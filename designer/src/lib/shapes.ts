import SETTINGS from "../input/settings";
import { PointTransformer } from "./pointTransformer";
import type { Point } from "../types";

const pointTransformer = new PointTransformer(SETTINGS.photo, SETTINGS.real);

export class Line {
  constructor(private start: Point, private end: Point) {}

  getLength() {
    const dx = Math.abs(this.end.x - this.start.x);
    const dy = Math.abs(this.end.y - this.start.y);

    return Math.sqrt(dx * dx + dy * dy);
  }

  draw(ctx: CanvasRenderingContext2D, lineWidth: number, color: string) {
    ctx.strokeStyle = color;
    ctx.lineWidth = lineWidth;

    ctx.beginPath();
    ctx.moveTo(this.start.x, this.start.y);
    ctx.lineTo(this.end.x, this.end.y);
    ctx.stroke();
  }

  toProgram() {
    const realStart = pointTransformer.transformPoint(this.start);
    const realEnd = pointTransformer.transformPoint(this.end);

    const realShape = new Line(realStart, realEnd);

    const length = realShape.getLength();

    return `LINE ${length.toFixed(2)}`;
  }
}

export class Arc {
  constructor(
    private start: Point,
    private middle: Point,
    private end: Point
  ) {}

  getRadius(): number {
    // Calculate the radius of the arc
    const a = Math.sqrt(
      Math.pow(this.end.x - this.middle.x, 2) +
        Math.pow(this.end.y - this.middle.y, 2)
    );
    const b = Math.sqrt(
      Math.pow(this.start.x - this.middle.x, 2) +
        Math.pow(this.start.y - this.middle.y, 2)
    );
    const c = Math.sqrt(
      Math.pow(this.end.x - this.start.x, 2) +
        Math.pow(this.end.y - this.start.y, 2)
    );

    const s = (a + b + c) / 2; // semi-perimeter

    const radius =
      (a * b * c) / (4 * Math.sqrt(s * (s - a) * (s - b) * (s - c))); // radius of the circumscribed circle

    return radius;
  }

  getAngles(): { startAngle: number; endAngle: number } {
    const center = this.getCenter();

    let startAngle = Math.atan2(
      this.start.y - center.y,
      this.start.x - center.x
    );
    let midAngle = Math.atan2(
      this.middle.y - center.y,
      this.middle.x - center.x
    );
    let endAngle = Math.atan2(this.end.y - center.y, this.end.x - center.x);

    // Ensure the angles are in the range [0, 2π]
    if (startAngle < 0) startAngle += 2 * Math.PI;
    if (midAngle < 0) midAngle += 2 * Math.PI;
    if (endAngle < 0) endAngle += 2 * Math.PI;

    // Swap the start and end angles if necessary to ensure the arc passes through the middle point
    if (
      (startAngle < endAngle &&
        (midAngle < startAngle || midAngle > endAngle)) ||
      (startAngle > endAngle && midAngle < startAngle && midAngle > endAngle)
    ) {
      const temp = startAngle;
      startAngle = endAngle;
      endAngle = temp;
    }

    return { startAngle, endAngle };
  }

  getCenter(): Point {
    // Calculate the center of the arc
    const d =
      2 *
      (this.start.x * (this.middle.y - this.end.y) +
        this.middle.x * (this.end.y - this.start.y) +
        this.end.x * (this.start.y - this.middle.y));

    const ux =
      ((Math.pow(this.start.x, 2) + Math.pow(this.start.y, 2)) *
        (this.middle.y - this.end.y) +
        (Math.pow(this.middle.x, 2) + Math.pow(this.middle.y, 2)) *
          (this.end.y - this.start.y) +
        (Math.pow(this.end.x, 2) + Math.pow(this.end.y, 2)) *
          (this.start.y - this.middle.y)) /
      d;
    const uy =
      ((Math.pow(this.start.x, 2) + Math.pow(this.start.y, 2)) *
        (this.end.x - this.middle.x) +
        (Math.pow(this.middle.x, 2) + Math.pow(this.middle.y, 2)) *
          (this.start.x - this.end.x) +
        (Math.pow(this.end.x, 2) + Math.pow(this.end.y, 2)) *
          (this.middle.x - this.start.x)) /
      d;

    return { x: ux, y: uy };
  }

  getLength(): number {
    const radius = this.getRadius();
    const angles = this.getAngles();

    // Calculate the difference between the start and end angles
    let angleDiff = angles.endAngle - angles.startAngle;

    // Ensure the angle is positive and less than 2*PI
    if (angleDiff < 0) {
      angleDiff += 2 * Math.PI;
    } else if (angleDiff > 2 * Math.PI) {
      angleDiff -= 2 * Math.PI;
    }

    // Calculate the length of the arc
    const length = radius * angleDiff;

    return length;
  }

  draw(ctx: CanvasRenderingContext2D, lineWidth: number, color: string) {
    ctx.strokeStyle = color;
    ctx.lineWidth = lineWidth;

    const center = this.getCenter();
    const radius = this.getRadius();
    const angles = this.getAngles();

    ctx.beginPath();
    ctx.arc(center.x, center.y, radius, angles.startAngle, angles.endAngle);
    ctx.stroke();
  }

  toProgram() {
    const realStart = pointTransformer.transformPoint(this.start);
    const realMiddle = pointTransformer.transformPoint(this.middle);
    const realEnd = pointTransformer.transformPoint(this.end);

    const realShape = new Arc(realStart, realMiddle, realEnd);

    const radius = realShape.getRadius();
    const length = realShape.getLength();

    return `ARC ${radius.toFixed(2)} ${length.toFixed(2)}`;
  }
}
