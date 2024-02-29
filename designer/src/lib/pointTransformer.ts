import type { Dimensions, Point } from "../types";

export class PointTransformer {
  private widthRatio: number;
  private heightRatio: number;

  constructor(originalSquare: Dimensions, targetSquare: Dimensions) {
    this.widthRatio = targetSquare.width / originalSquare.width;
    this.heightRatio = targetSquare.height / originalSquare.height;
  }

  public transformPoint(point: Point): Point {
    return {
      x: point.x * this.widthRatio,
      y: point.y * this.heightRatio,
    };
  }
}
