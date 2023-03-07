<script>
  import G6 from "@antv/g6";
  import { onMount } from "svelte";

  export let data;
  onMount(() => {
    const container = document.getElementById("graph-container");
    const graph = new G6.Graph({
      container,
      width: 800,
      height: 500,
    });
    graph.data(data); // 读取数据源到图上
    graph.render(); // 渲染图
  });
</script>

<div class=" font-thin bg-red-50 text-center">ddy‘s test demo</div>
<div id="graph-container" class=" container mx-auto bg-blue-100 px-4 py-4" />
