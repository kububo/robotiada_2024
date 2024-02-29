<script lang="ts">
  import ToolPicker from "./components/ToolPicker.svelte";
  import Canvas from "./components/Canvas.svelte";
  import Output from "./components/Output.svelte";

  import SETTINGS from "./input/settings";
  import { getImage } from "./lib/getImage";
  import { state } from "./state";

  getImage()
    .then((image: HTMLImageElement) => {
      $state.image = image;
    })
    .catch((message: string) => alert("Error: " + message));
</script>

<ToolPicker />
<Canvas />
<Output />

<style>
  :global(body) {
    font-family: Arial, Helvetica, sans-serif;
  }
</style>
