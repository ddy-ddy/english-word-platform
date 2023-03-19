<script>
  import G6 from "@antv/g6";
  import { onMount } from "svelte";
  export let data;
  const colors = {
    B: "#5B8FF9",
    R: "#F46649",
    Y: "#EEBC20",
    G: "#5BD8A6",
    DI: "#A7A7A7",
  };

  //  组件props
  const props = {
    data: data,
    config: {
      padding: [20, 50],
      defaultLevel: 3,
      defaultZoom: 0.5,
      modes: { default: ["zoom-canvas", "drag-canvas"] },
    },
  };
  // 自定义节点、边
  const registerFn = () => {
    G6.registerNode(
      "flow-rect", // node name
      {
        shapeType: "flow-rect",

        draw(cfg, group) {
          /**
           * 绘制节点，包含文本
           * @param  {Object} cfg 节点的配置项
           * @param  {G.Group} group 图形分组，节点中的图形对象的容器
           * @return {G.Shape} 绘制的图形，通过 node.get('keyShape') 可以获取到
           */
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
                text: name,
                fontSize: 18,
                fill: "#000",
                opacity: 0.85,
              },
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
    G6.registerEdge(
      "flow-cubic",
      {
        draw(cfg, group) {},
        getControlPoints(cfg) {
          let controlPoints = cfg.controlPoints; // 指定controlPoints
          if (!controlPoints || !controlPoints.length) {
            const { startPoint, endPoint, sourceNode, targetNode } = cfg;
            const {
              x: startX,
              y: startY,
              coefficientX,
              coefficientY,
            } = sourceNode ? sourceNode.getModel() : startPoint;
            const { x: endX, y: endY } = targetNode
              ? targetNode.getModel()
              : endPoint;
            let curveStart = (endX - startX) * coefficientX;
            let curveEnd = (endY - startY) * coefficientY;
            curveStart = curveStart > 40 ? 40 : curveStart;
            curveEnd = curveEnd < -30 ? curveEnd : -30;
            controlPoints = [
              { x: startPoint.x + curveStart, y: startPoint.y },
              { x: endPoint.x + curveEnd, y: endPoint.y },
            ];
          }
          return controlPoints;
        },
        getPath(points) {
          const path = [];
          path.push(["M", points[0].x, points[0].y]);
          path.push([
            "C",
            points[1].x,
            points[1].y,
            points[2].x,
            points[2].y,
            points[3].x,
            points[3].y,
          ]);
          return path;
        },
      },
      "single-line"
    );
  };

  onMount(() => {
    const container = document.getElementById("graph-container");
    const width = container.scrollWidth;
    const height = container.scrollHeight || 1500;
    // 工具栏的位置
    const toolbar = new G6.ToolBar({
      position: { x: 20, y: 80 },
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
          style: {
            fill: "#000",
            fontSize: 12,
            fontWeight: "bold",
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

    registerFn();

    const { data } = props;
    let graph = null;

    const initGraph = (data) => {
      if (!data) {
        return;
      }
      const { onInit, config } = props;
      // 提示栏
      const tooltip = new G6.Tooltip({
        // offsetX and offsetY include the padding of the parent container
        offsetX: 20,
        offsetY: 30,
        // the types of items that allow the tooltip show up
        // 允许出现 tooltip 的 item 类型
        itemTypes: ["node"],
        // custom the tooltip's content
        // 自定义 tooltip 内容
        getContent: (e) => {
          const outDiv = document.createElement("div");
          //outDiv.style.padding = '0px 0px 20px 0px';
          const nodeInfo = e.item.getModel().label;
          let formatedNodeInfo = "";
          for (let i = 0; i < nodeInfo.length; i++) {
            formatedNodeInfo = `${formatedNodeInfo}${nodeInfo[i]}`;
            if (i !== 0 && i % 30 === 0)
              formatedNodeInfo = `${formatedNodeInfo}<br/>`;
          }
          outDiv.innerHTML = `${formatedNodeInfo}`;
          return outDiv;
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
      graph = new G6.TreeGraph({
        container,
        ...defaultConfig,
        ...config,
        plugins: [tooltip, toolbar],
        linkCenter: true,
        // 设置为true，启用 redo & undo 栈功能
        enabledStack: true,
      });

      if (typeof onInit === "function") {
        onInit(graph);
      }
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

    initGraph(data);

    if (typeof window !== "undefined")
      window.onresize = () => {
        if (!graph || graph.get("destroyed")) return;
        if (!container || !container.scrollWidth || !container.scrollHeight)
          return;
        graph.changeSize(container.scrollWidth, container.scrollHeight);
      };
  });
</script>

<div class="grid-for-background full-screen">
  <!-- navbar -->
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
            <input
              type="text"
              placeholder="输入你要查询的单词..."
              class="input input-bordered bg-base-200"
            />
            <button class="btn btn-square">
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

  <!-- graph-container -->
  <div class="bg-base-50 full-screen">
    <div id="graph-container" />
  </div>
</div>

<style>
  .grid-for-background {
    background-image: linear-gradient(
        to right,
        #cccccc 0.6px,
        transparent 0.6px
      ),
      linear-gradient(to bottom, #cccccc 0.6px, transparent 0.6px);
    background-size: 50px 50px;
  }
</style>
