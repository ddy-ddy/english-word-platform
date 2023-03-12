<script>
  import G6 from "@antv/g6";
  import { onMount } from "svelte";
  import insertCss from "insert-css";

  insertCss(`
  .g6-component-toolbar li {
    list-style-type: none !important;
  }
`);
  export let data;

  onMount(() => {
    G6.registerNode("card-node", {
      draw: function drawShape(cfg, group) {
        const r = 2;
        const color = "#5B8FF9";
        const w = cfg.size[0];
        const h = cfg.size[1];
        const shape = group.addShape("rect", {
          attrs: {
            x: -w / 2,
            y: -h / 2,
            width: w, //200,
            height: h, // 60
            stroke: color,
            radius: r,
            fill: "#fff",
          },
          // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
          name: "main-box",
          draggable: true,
        });

        group.addShape("rect", {
          attrs: {
            x: -w / 2,
            y: -h / 2,
            width: w, //200,
            height: h / 2, // 60
            fill: color,
            radius: [r, r, 0, 0],
          },
          // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
          name: "title-box",
          draggable: true,
        });

        // title text
        group.addShape("text", {
          attrs: {
            textBaseline: "top",
            x: -w / 2 + 8,
            y: -h / 2 + 2,
            lineHeight: 20,
            text: cfg.id,
            fill: "#fff",
          },
          // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
          name: "title",
        });
        cfg.children &&
          group.addShape("marker", {
            attrs: {
              x: w / 2,
              y: 0,
              r: 6,
              cursor: "pointer",
              symbol: cfg.collapsed ? G6.Marker.expand : G6.Marker.collapse,
              stroke: "#666",
              lineWidth: 1,
              fill: "#fff",
            },
            // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
            name: "collapse-icon",
          });
        group.addShape("text", {
          attrs: {
            textBaseline: "top",
            x: -w / 2 + 8,
            y: -h / 2 + 24,
            lineHeight: 20,
            text: "description",
            fill: "rgba(0,0,0, 1)",
          },
          // must be assigned in G6 3.3 and later versions. it can be any string you want, but should be unique in a custom item type
          name: `description`,
        });
        return shape;
      },
      setState(name, value, item) {
        if (name === "collapsed") {
          const marker = item
            .get("group")
            .find((ele) => ele.get("name") === "collapse-icon");
          const icon = value ? G6.Marker.expand : G6.Marker.collapse;
          marker.attr("symbol", icon);
        }
      },
    });
    const container = document.getElementById("graph-container");
    const width = container.scrollWidth;
    const height = container.scrollHeight || 500;
    const toolbar = new G6.ToolBar({
      position: { x: 50, y: 100 },
    });
    const graph = new G6.TreeGraph({
      container,
      width,
      height,
      plugins: [toolbar],
      linkCenter: true,
      enabledStack: true,
      modes: {
        default: ["drag-canvas"],
      },
      defaultNode: {
        type: "card-node",
        size: [100, 40],
      },
      defaultEdge: {
        type: "cubic-horizontal",
        style: {
          endArrow: true,
        },
      },
      layout: {
        type: "indented",
        direction: "LR",
        dropCap: false,
        indent: 200,
        getHeight: () => {
          return 60;
        },
      },
    });

    graph.data(data);
    graph.render();
    graph.fitView();
    graph.on("node:click", (e) => {
      if (e.target.get("name") === "collapse-icon") {
        e.item.getModel().collapsed = !e.item.getModel().collapsed;
        graph.setItemState(e.item, "collapsed", e.item.getModel().collapsed);
        graph.layout();
      }
    });
  });
</script>

<div class="grid-bg full-screen">
  <!-- navbar -->
  <div class="mx-4">
    <div class="navbar bg-base-100 top-4 shadow-xl shadow-blue-200 rounded-md">
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
