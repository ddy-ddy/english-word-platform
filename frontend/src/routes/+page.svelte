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
      defaultZoom: 0.8,
      modes: { default: ["zoom-canvas", "drag-canvas"] },
    },
  };
  // 自定义节点、边
  const registerFn = () => {
    /**
     * 自定义节点
     */
    G6.registerNode(
      "flow-rect",
      {
        shapeType: "flow-rect",
        draw(cfg, group) {
          const {
            name = "",
            variableName,
            variableValue,
            variableUp,
            label,
            collapsed,
            currency,
            status,
            rate,
          } = cfg;

          const grey = "#CED4D9";
          const rectConfig = {
            width: 202,
            height: 60,
            lineWidth: 1,
            fontSize: 12,
            fill: "#fff",
            radius: 4,
            stroke: grey,
            opacity: 1,
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

          // label title
          group.addShape("text", {
            attrs: {
              ...textConfig,
              x: 12 + nodeOrigin.x,
              y: 20 + nodeOrigin.y,
              text: name.length > 28 ? name.substr(0, 28) + "..." : name,
              fontSize: 12,
              opacity: 0.85,
              fill: "#000",
              cursor: "pointer",
            },
            // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
            name: "name-shape",
          });

          // price
          const price = group.addShape("text", {
            attrs: {
              ...textConfig,
              x: 12 + nodeOrigin.x,
              y: rectBBox.maxY - 12,
              text: label,
              fontSize: 16,
              fill: "#000",
              opacity: 0.85,
            },
          });

          // label currency
          group.addShape("text", {
            attrs: {
              ...textConfig,
              x: price.getBBox().maxX + 5,
              y: rectBBox.maxY - 12,
              text: currency,
              fontSize: 12,
              fill: "#000",
              opacity: 0.75,
            },
          });

          // percentage
          const percentText = group.addShape("text", {
            attrs: {
              ...textConfig,
              x: rectBBox.maxX - 8,
              y: rectBBox.maxY - 12,
              text: `${((variableValue || 0) * 100).toFixed(2)}%`,
              fontSize: 12,
              textAlign: "right",
              fill: colors[status],
            },
          });

          // percentage triangle
          const symbol = variableUp ? "triangle" : "triangle-down";
          const triangle = group.addShape("marker", {
            attrs: {
              ...textConfig,
              x: percentText.getBBox().minX - 10,
              y: rectBBox.maxY - 12 - 6,
              symbol,
              r: 6,
              fill: colors[status],
            },
          });

          // variable name
          group.addShape("text", {
            attrs: {
              ...textConfig,
              x: triangle.getBBox().minX - 4,
              y: rectBBox.maxY - 12,
              text: variableName,
              fontSize: 12,
              textAlign: "right",
              fill: "#000",
              opacity: 0.45,
            },
          });

          // bottom line background
          const bottomBackRect = group.addShape("rect", {
            attrs: {
              x: nodeOrigin.x,
              y: rectBBox.maxY - 4,
              width: rectConfig.width,
              height: 4,
              radius: [0, 0, rectConfig.radius, rectConfig.radius],
              fill: "#E0DFE3",
            },
          });

          // bottom percent
          const bottomRect = group.addShape("rect", {
            attrs: {
              x: nodeOrigin.x,
              y: rectBBox.maxY - 4,
              width: rate * rectBBox.width,
              height: 4,
              radius: [0, 0, 0, rectConfig.radius],
              fill: colors[status],
            },
          });

          // collapse rect
          if (cfg.children && cfg.children.length) {
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
              // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
              name: "collapse-back",
              modelId: cfg.id,
            });

            // collpase text
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
              // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
              name: "collapse-text",
              modelId: cfg.id,
            });
          }

          this.drawLinkPoints(cfg, group);
          return rect;
        },
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
    const toolbar = new G6.ToolBar({
      position: { x: 850, y: 80 },
    });
    // 默认配置
    const defaultConfig = {
      width,
      height,
      modes: {
        default: ["zoom-canvas", "drag-canvas"],
      },
      fitView: true,
      animate: true,
      defaultNode: {
        type: "flow-rect",
      },
      defaultEdge: {
        type: "cubic-horizontal",
        style: {
          stroke: "#CED4D9",
        },
      },
      layout: {
        type: "indented",
        direction: "LR",
        dropCap: false,
        indent: 300,
        getHeight: () => {
          return 60;
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
          const nodeName = e.item.getModel().name;
          let formatedNodeName = "";
          for (let i = 0; i < nodeName.length; i++) {
            formatedNodeName = `${formatedNodeName}${nodeName[i]}`;
            if (i !== 0 && i % 20 === 0)
              formatedNodeName = `${formatedNodeName}<br/>`;
          }
          outDiv.innerHTML = `${formatedNodeName}`;
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
    background-image: linear-gradient(to right, #cccccc 0.6px, transparent 0.6px),
      linear-gradient(to bottom, #cccccc 0.6px, transparent 0.6px);
    background-size: 40px 50px;
  }
</style>
