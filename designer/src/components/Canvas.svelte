<script lang="ts">
  import { canvasClicked } from "../lib/canvasClicked";
  import { drawPoint } from "../lib/drawPoint";
  import { state } from "../state";

  let canvas: HTMLCanvasElement;
  let ctx: CanvasRenderingContext2D;

  state.subscribe((value) => {
    if (!canvas || !value.image) return;
    if (!ctx) ctx = canvas.getContext("2d")!;

    canvas.width = value.image.width;
    canvas.height = value.image.height;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(value.image, 0, 0, canvas.width, canvas.height);

    value.currentPoints.forEach((point) => drawPoint(ctx, point, 5, "purple"));
    value.shapes.forEach((shape) => shape.draw(ctx, 5, "green"));
  });
</script>

<div class="container">
  <canvas bind:this={canvas} on:click={canvasClicked} />
</div>

<style>
  .container {
    display: flex;
    width: 100%;
  }

  canvas {
    cursor: crosshair;
    outline: 1px solid black;
    margin: 1rem auto;
  }
</style>
