<script>
  import G6 from "@antv/g6";
  import { onMount } from "svelte";

  export let data;
  onMount(() => {
    const container = document.getElementById("graph-container");
    // 实例化 grid 插件
    const graph = new G6.Graph({
      container,
      width: 800,
      height: 600,
      // 节点默认配置
      defaultNode: {
        labelCfg: {
          style: {
            fill: "#fff",
          },
        },
      },
      // 边默认配置
      defaultEdge: {
        labelCfg: {
          autoRotate: true,
        },
      },
      // 节点在各状态下的样式
      nodeStateStyles: {
        // hover 状态为 true 时的样式
        hover: {
          fill: "lightsteelblue",
        },
        // click 状态为 true 时的样式
        click: {
          stroke: "#000",
          lineWidth: 3,
        },
      },
      // 边在各状态下的样式
      edgeStateStyles: {
        // click 状态为 true 时的样式
        click: {
          stroke: "steelblue",
        },
      },
      // 布局
      layout: {
        type: "force",
        linkDistance: 100,
        preventOverlap: true,
        nodeStrength: -30,
        edgeStrength: 0.1,
      },
      // 内置交互
      modes: {
        default: ["drag-canvas", "zoom-canvas", "drag-node"],
      },
      animate: true, // Boolean，可选，全局变化时否使用动画过渡

    });
    graph.data(data); // 读取数据源到图上
    graph.render(); // 渲染图

    // 监听鼠标进入节点
    graph.on("node:mouseenter", (e) => {
      const nodeItem = e.item;
      // 设置目标节点的 hover 状态 为 true
      graph.setItemState(nodeItem, "hover", true);
    });
    // 监听鼠标离开节点
    graph.on("node:mouseleave", (e) => {
      const nodeItem = e.item;
      // 设置目标节点的 hover 状态 false
      graph.setItemState(nodeItem, "hover", false);
    });
    // 监听鼠标点击节点
    graph.on("node:click", (e) => {
      // 先将所有当前有 click 状态的节点的 click 状态置为 false
      const clickNodes = graph.findAllByState("node", "click");
      clickNodes.forEach((cn) => {
        graph.setItemState(cn, "click", false);
      });
      const nodeItem = e.item;
      // 设置目标节点的 click 状态 为 true
      graph.setItemState(nodeItem, "click", true);
    });
    // 监听鼠标点击节点
    graph.on("edge:click", (e) => {
      // 先将所有当前有 click 状态的边的 click 状态置为 false
      const clickEdges = graph.findAllByState("edge", "click");
      clickEdges.forEach((ce) => {
        graph.setItemState(ce, "click", false);
      });
      const edgeItem = e.item;
      // 设置目标边的 click 状态 为 true
      graph.setItemState(edgeItem, "click", true);
    });
  });
</script>

<div class=" font-thin bg-red-50 text-center">test demo</div>
<div id="graph-container" class=" container mx-auto bg-blue-100 px-4 py-4" />
