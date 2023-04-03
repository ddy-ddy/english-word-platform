<script>
  import G6 from "@antv/g6";
  export let data; // 传入的配置数据
  let searchWord; // 搜索词
  let graph = null; // 图实例
  let showLegend = false; // 是否显示图例
  const nodeLegend = data["nodeLegend"]; // 节点图例
  const relationLegend = data["relationLegend"]; // 关系图例
  const colors = data["colors"]; // 节点颜色

  function renderGraph(useData) {
    if (graph) {
      graph.destroy();
    }
    const graphData = useData; // 图数据
    const container = document.getElementById("graph-container");
    const width = container.scrollWidth;
    const height = container.scrollHeight || 1500;
    // 图数据及配置
    const props = {
      data: graphData,
      config: {
        padding: [20, 50],
        defaultLevel: 3,
        defaultZoom: 0.5,
        modes: { default: ["zoom-canvas", "drag-canvas"] },
      },
    };
    // 工具栏
    const toolbar = new G6.ToolBar({
      position: { x: 50, y: 80 },
      getContent: () => {
        const outDiv = document.createElement("div");
        outDiv.style.width = "200px";
        outDiv.style.padding = "5px";
        outDiv.style.fontSize = "13px";
        // outDiv.style.backgroundColor = "rgb(241 245 249)";
        outDiv.style.fontWeight = "500";
        outDiv.innerHTML = `
        <ul class="grid grid-cols-4 justify-items-center items-center">
          <li code="zoomOut" class="rounded-lg pt-0.5 border-gray-300 text-center hover:bg-sky-200 active:bg-sky-300 hover:text-black">放大</li>
          <li code="zoomIn" class="rounded-lg pt-0.5 border-gray-300 text-center hover:bg-sky-200 active:bg-sky-300 hover:text-black">缩小</li>
          <li code="realZoom" class="rounded-lg pt-0.5  border-gray-300 text-center hover:bg-sky-200 active:bg-sky-300 hover:text-black">复位</li>
          <li code="show" class="rounded-lg pt-0.5 border-gray-300 text-center hover:bg-sky-200 active:bg-sky-300 hover:text-black">图例</li>
        </ul>`;
        return outDiv;
      },
      handleClick: (code, graph) => {
        if (code === "zoomIn") {
          toolbar.zoomIn();
        } else if (code === "zoomOut") {
          toolbar.zoomOut();
        } else if (code === "realZoom") {
          toolbar.realZoom();
        } else if (code === "show") {
          if (showLegend === true) {
            showLegend = false;
          } else {
            showLegend = true;
          }
        }
      },
    });
    // 默认配置
    const defaultConfig = {
      width,
      height,
      modes: {
        default: ["zoom-canvas", "drag-canvas"],
      },
      fitView: true, // 图自动适配画布大小
      fitViewPadding: [-800, 300, 0, 300], // 图自动适配画布大小时的边距
      animate: true,
      minZoom: 0.4, // 最小缩放比例
      maxZoom: 2, // 最大缩放比例
      defaultNode: {
        type: "flow-rect",
      },
      defaultEdge: {
        type: "cubic-horizontal",
        style: {
          stroke: "#CED4D9",
          lineWidth: 2,
        },
        labelCfg: {
          refY: 10,
          autoRotate: true,
          style: {
            fontSize: 12,
            fontWeight: "thin",
          },
        },
        label: "relation",
      },
      layout: {
        type: "indented",
        direction: "LR",
        dropCap: false, // 每个节点的第一个自节点是否位于下一行
        indent: 300, //同一层节点之间的宽间距
        getHeight: () => {
          return 60; //每个节点的高度
        },
      },
    };
    // 自定义节点
    const registerFn = () => {
      G6.registerNode(
        "flow-rect", // node name
        {
          shapeType: "flow-rect",
          draw(cfg, group) {
            const { nodeType, name, label, collapsed, status } = cfg;
            const rectConfig = {
              width: 150,
              height: 60,
              lineWidth: 1,
              fontSize: 12,
              fill: "#fff", // 背景颜色
              radius: 4,
              stroke: "#CED4D9", // 边框颜色
              opacity: 1, // 透明度
            };
            const nodeOrigin = {
              x: -rectConfig.width / 2,
              y: -rectConfig.height / 2,
            };
            const textConfig = {
              textAlign: "left",
              textBaseline: "bottom",
            };
            const rect = group.addShape("rect", {
              attrs: {
                x: nodeOrigin.x,
                y: nodeOrigin.y,
                ...rectConfig,
              },
            });
            const rectBBox = rect.getBBox();
            if (nodeType === "query") {
              group.addShape("text", {
                attrs: {
                  ...textConfig,
                  x: nodeOrigin.x / 2 + 4,
                  y: nodeOrigin.y + 36,
                  text: name,
                  fontSize: 18,
                  fill: "#000",
                  opacity: 0.85,
                },
              });
            } else {
              // 单词名称
              group.addShape("text", {
                attrs: {
                  ...textConfig,
                  x: 12 + nodeOrigin.x,
                  y: 24 + nodeOrigin.y,
                  text: name.indexOf(",") !== -1 ? name.split(",")[0] : name,
                  fontSize: 18,
                  fill: "#000",
                  cursor: "pointer",
                  opacity: 0.85,
                },
                name: "full-name-shape",
              });
              // 单词词性+释义
              group.addShape("text", {
                attrs: {
                  ...textConfig,
                  x: 12 + nodeOrigin.x,
                  y: 50 + nodeOrigin.y,
                  text: label.length > 20 ? label.substr(0, 20) + "..." : label,
                  fontSize: 12,
                  opacity: 0.85,
                  fill: "#000",
                  cursor: "pointer",
                },
                name: "name-shape",
              });
            }
            // 底部颜色条
            group.addShape("rect", {
              attrs: {
                x: nodeOrigin.x,
                y: rectBBox.maxY - 4,
                width: rectBBox.width - 1,
                height: 5,
                radius: [0, 0, rectConfig.radius, rectConfig.radius],
                fill: colors[status],
              },
            });
            if (cfg.children && cfg.children.length) {
              // 指针样式
              group.addShape("rect", {
                attrs: {
                  x: rectConfig.width / 2 - 8,
                  y: -8,
                  width: 16,
                  height: 16,
                  stroke: "rgba(0, 0, 0, 0.25)",
                  cursor: "pointer",
                  fill: "#fff",
                },
                name: "collapse-back",
                modelId: cfg.id,
              });
              // 指针文本
              group.addShape("text", {
                attrs: {
                  x: rectConfig.width / 2,
                  y: -1,
                  textAlign: "center",
                  textBaseline: "middle",
                  text: collapsed ? "+" : "-",
                  fontSize: 16,
                  cursor: "pointer",
                  fill: "rgba(0, 0, 0, 0.25)",
                },
                name: "collapse-text",
                modelId: cfg.id,
              });
            }
            this.drawLinkPoints(cfg, group);
            return rect;
          },
          //更新节点后的操作
          update(cfg, item) {
            const { level, status, name } = cfg;
            const group = item.getContainer();
            let mask = group.find((ele) => ele.get("name") === "mask-shape");
            let maskLabel = group.find(
              (ele) => ele.get("name") === "mask-label-shape"
            );
            if (level === 0) {
              group.get("children").forEach((child) => {
                if (child.get("name")?.includes("collapse")) return;
                child.hide();
              });
              if (!mask) {
                mask = group.addShape("rect", {
                  attrs: {
                    x: -101,
                    y: -30,
                    width: 202,
                    height: 60,
                    opacity: 0,
                    fill: colors[status],
                  },
                  // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
                  name: "mask-shape",
                });
                maskLabel = group.addShape("text", {
                  attrs: {
                    fill: "#fff",
                    fontSize: 20,
                    x: 0,
                    y: 10,
                    text: name.length > 28 ? name.substr(0, 16) + "..." : name,
                    textAlign: "center",
                    opacity: 0,
                  },
                  // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
                  name: "mask-label-shape",
                });
                const collapseRect = group.find(
                  (ele) => ele.get("name") === "collapse-back"
                );
                const collapseText = group.find(
                  (ele) => ele.get("name") === "collapse-text"
                );
                collapseRect?.toFront();
                collapseText?.toFront();
              } else {
                mask.show();
                maskLabel.show();
              }
              mask.animate({ opacity: 1 }, 200);
              maskLabel.animate({ opacity: 1 }, 200);
              return mask;
            } else {
              group.get("children").forEach((child) => {
                if (child.get("name")?.includes("collapse")) return;
                child.show();
              });
              mask?.animate(
                { opacity: 0 },
                {
                  duration: 200,
                  callback: () => mask.hide(),
                }
              );
              maskLabel?.animate(
                { opacity: 0 },
                {
                  duration: 200,
                  callback: () => maskLabel.hide(),
                }
              );
            }
            this.updateLinkPoints(cfg, group);
          },
          // 设置节点状态
          setState(name, value, item) {
            if (name === "collapse") {
              const group = item.getContainer();
              const collapseText = group.find(
                (e) => e.get("name") === "collapse-text"
              );
              if (collapseText) {
                if (!value) {
                  collapseText.attr({
                    text: "-",
                  });
                } else {
                  collapseText.attr({
                    text: "+",
                  });
                }
              }
            }
          },
          //获取锚点(相关边的接入点)
          getAnchorPoints() {
            return [
              [0, 0.5],
              [1, 0.5],
            ];
          },
        },
        "rect"
      );
    };
    // 初始化图
    const initGraph = (data) => {
      console.log(data);
      if (!data) {
        return;
      }
      // 提示栏
      const tooltip = new G6.Tooltip({
        offsetX: 20,
        offsetY: 30,
        // 允许出现 tooltip 的 item 类型
        itemTypes: ["node"],
        // 自定义 tooltip 内容
        getContent: (e) => {
          // const outDiv = document.createElement("div");
          const nodeInfo = e.item.getModel().label;
          const nodeName = e.item.getModel().name;
          const nodeExamples = eval(e.item.getModel().examples);
          return `<div class="bg-base-100">
                    <ul class="space-y-4">
                      <li class="text-lg font-mono italic font-semibold underline decoration-sky-500 underline-offset-4 ">${nodeName}</li>
                      <li class="text-xs font-mono font-light">${nodeInfo}</li>
                      <ul class="list-disc list-inside">
                        ${nodeExamples
                          .map(
                            (example) =>
                              `<li class="text-xs font-mono font-light">${example}</li>`
                          )
                          .join("")}  
                      </ul>
                    </ul>
                  </div>`;
        },
        shouldBegin: (e) => {
          if (
            e.target.get("name") === "name-shape" ||
            e.target.get("name") === "mask-label-shape"
          )
            return true;
          return false;
        },
      });
      // 初始化画布
      graph = new G6.TreeGraph({
        container,
        ...defaultConfig,
        ...props.config,
        plugins: [tooltip, toolbar],
        linkCenter: true,
        enabledStack: true,
      });
      // 新增边名
      graph.edge(function (edge) {
        const node1 = graph
          .getNodes()
          .filter((n) => n.getID() === edge["target"]);
        const model = node1[0].getModel();
        const relation = model["relation"];
        return {
          label: relation,
        };
      });
      graph.data(data);
      graph.render();
      const handleCollapse = (e) => {
        const target = e.target;
        const id = target.get("modelId");
        const item = graph.findById(id);
        const nodeModel = item.getModel();
        nodeModel.collapsed = !nodeModel.collapsed;
        graph.layout();
        graph.setItemState(item, "collapse", nodeModel.collapsed);
      };
      graph.on("collapse-text:click", (e) => {
        handleCollapse(e);
      });
      graph.on("collapse-back:click", (e) => {
        handleCollapse(e);
      });
    };
    registerFn();
    initGraph(props.data);
  }

  async function handleSubmit() {
    const formData = new FormData();
    formData.append("word", searchWord);
    const response = await fetch("http://127.0.0.1:5002/search", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();
    renderGraph(result);
  }
</script>

<div class="grid-for-background full-screen">
  <!-- Navbar -->
  <div class="mx-4">
    <div class="navbar bg-base-100 top-4 shadow-lg shadow-blue-200 rounded-md">
      <!-- 最左边 -->
      <div class="navbar-start">
        <a class="btn btn-ghost normal-case text-xl">English KG</a>
      </div>
      <!-- 中间搜索 -->
      <div class="navbar-center">
        <div class="form-control">
          <div class="input-group">
            <form on:submit|preventDefault={handleSubmit}>
              <input
                type="text"
                placeholder="输入你要查询的单词..."
                class="input input-bordered bg-base-200"
                bind:value={searchWord}
              />
              <button type="submit" class="btn btn-square">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  ><path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  /></svg
                >
              </button>
            </form>
          </div>
        </div>
      </div>
      <!-- 最右边 -->
      <div class="navbar-end">
        <ul class="menu menu-horizontal px-1">
          <li><a>网站介绍</a></li>
          <li><a>关于我</a></li>
        </ul>
      </div>
    </div>
  </div>
  <!-- Legend -->
  {#if showLegend}
    <div
      id="showLegend"
      class="transition slide-in fixed bottom-24 left-12 card w-56 bg-slate-100 shadow-xl"
    >
      <div class="card-body p-6">
        <div class="table w-full top-2">
          <div class="table-row-group">
            {#each nodeLegend as info}
              <div class="table-row">
                <div class="table-cell text-center">
                  <span class=" {info[1]} font-black ">—————— </span>
                </div>
                <div class="table-cell text-left font-normal tracking-wide">
                  {info[0]}
                </div>
              </div>
            {/each}
            {#each relationLegend as info}
              <div class="table-row">
                <div class="table-cell text-center font-mono font-normal ">
                  {info[0]}
                </div>
                <div class="table-cell text-left font-normal tracking-wide">
                  {info[1]}
                </div>
              </div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  {/if}
  <!-- graph-container -->
  <div class="bg-base-50 full-screen">
    <div id="graph-container" />
  </div>
</div>

<style>
  /* 网格化背景 */
  .grid-for-background {
    background-image: linear-gradient(
        to right,
        #cccccc 0.6px,
        transparent 0.6px
      ),
      linear-gradient(to bottom, #cccccc 0.6px, transparent 0.6px);
    background-size: 50px 50px;
  }
  /* 图例显示的动画 */
  .transition {
    transition-property: all;
    transition-duration: 0.5s;
    transition-timing-function: ease;
  }

  @keyframes slide-in {
    from {
      opacity: 0;
      transform: translateX(-100%);
    }
    to {
      opacity: 1;
      transform: translateX(0%);
    }
  }
  @keyframes slide-out {
    from {
      opacity: 1;
      transform: translateX(0%);
    }
    to {
      opacity: 0;
      transform: translateX(100%);
    }
  }

  .slide-in {
    animation-name: slide-in;
    animation-duration: 0.5s;
    animation-timing-function: ease;
  }
  .slide-out {
    animation-name: slide-out;
    animation-duration: 0.5s;
    animation-timing-function: ease;
  }
</style>
