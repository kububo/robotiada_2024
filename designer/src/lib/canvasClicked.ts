import { state } from "../state";
import { Line, Arc } from "./shapes";

export function canvasClicked(e: MouseEvent) {
  const target = e.target as HTMLCanvasElement;
  const bounding = target.getBoundingClientRect();

  const x = e.x - bounding.x;
  const y = e.y - bounding.y;

  const clickedPoint = { x, y };

  state.update((value) => {
    let shapeToAdd: Line | Arc | undefined = undefined;

    if (value.currentTool === "line" && value.currentPoints.length === 1) {
      shapeToAdd = new Line(value.currentPoints[0], clickedPoint);
    }

    if (value.currentTool === "arc" && value.currentPoints.length === 2) {
      shapeToAdd = new Arc(
        value.currentPoints[0],
        value.currentPoints[1],
        clickedPoint
      );
    }

    if (shapeToAdd) {
      return {
        ...value,
        currentPoints: [clickedPoint],
        shapes: [...value.shapes, shapeToAdd],
      };
    }

    return {
      ...value,
      currentPoints: [...value.currentPoints, clickedPoint],
    };
  });
}
