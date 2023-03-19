<script>
  import G6 from "@antv/g6";
  import { onMount } from "svelte";

  const data = {
    id: "1",
    label: "Modeling Methods",
    children: [
      {
        id: "2",
        label: "Classification",
        children: [
          {
            id: "3",
            label: "Logistic regression",
          },
        ],
      },
    ],
    edges: [
      {
        source: "1",
        target: "2",
        label: "relation1",
      },
      {
        source: "2",
        target: "3",
        label: "relation2",
      },
    ],
  };

  onMount(() => {
    const container = document.getElementById("container");
    const treeGraph = new G6.TreeGraph({
      container,
      width: container.scrollWidth,
      height: container.scrollHeight || 1500,
      modes: {
        default: ["drag-canvas", "zoom-canvas", "drag-node"],
      },
      defaultNode: {
        shape: "rect",
        style: {
          fill: "#C6E5FF",
          stroke: "#5B8FF9",
        },
        labelCfg: {
          style: {
            fill: "#000000",
            fontSize: 12,
          },
          position: "center",
        },
      },
      defaultEdge: {
        shape: "cubic-horizontal",
        style: {
          stroke: "#A3B1BF",
        },
        labelCfg: {
          style: {
            fill: "#000000",
            fontSize: 12,
          },
          position: "center",
        },
        label: 123,
      },
      layout: {
        type: "compactBox",
        direction: "LR",
        getId: function getId(d) {
          return d.id;
        },
        getHeight: function getHeight() {
          return 16;
        },
        getWidth: function getWidth() {
          return 16;
        },
        getVGap: function getVGap() {
          return 10;
        },
        getHGap: function getHGap() {
          return 100;
        },
      },
    });
    treeGraph.data(data);
    treeGraph.render();
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
    <div id="container" />
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
