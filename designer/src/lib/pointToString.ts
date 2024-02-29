import type { Point } from "../types";

export function pointToString(point: Point) {
  return `${point.x},${point.y}`;
}
