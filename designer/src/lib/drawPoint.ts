import type { Point } from "../types";

export function drawPoint(
  ctx: CanvasRenderingContext2D,
  point: Point,
  radius: number,
  color: string
) {
  ctx.fillStyle = color;

  ctx.beginPath();
  ctx.arc(point.x, point.y, radius, 0, 2 * Math.PI);
  ctx.closePath();
  ctx.fill();
}
