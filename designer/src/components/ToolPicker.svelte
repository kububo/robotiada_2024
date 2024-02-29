<script lang="ts">
  import { state } from "../state";

  const removeLastPoint = () => {
    if ($state.currentPoints.length > 1) {
      $state.currentPoints = $state.currentPoints.slice(0, -1);
    }
  };

  const removeLastShape = () => {
    $state.shapes = $state.shapes.slice(0, -1);
  };
</script>

<nav>
  <div>Current Tool: {$state.currentTool}</div>

  <div class="space">
    <button on:click={() => ($state.currentTool = "line")}>Pick a Line</button>
    <button on:click={() => ($state.currentTool = "arc")}>Pick an Arc</button>
  </div>

  <div class="space">
    <button on:click={removeLastPoint}>Remove Last Point</button>
    <button on:click={removeLastShape}>Remove Last Shape</button>
  </div>
</nav>

<style>
  nav {
    display: flex;
    align-items: center;
    gap: 3rem;

    padding: 0.5rem;

    background-color: aquamarine;
    border-radius: 0.5rem;
  }

  .space {
    display: flex;
    gap: 0.5rem;
  }
</style>
