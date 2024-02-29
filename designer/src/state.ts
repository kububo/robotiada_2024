import { writable } from "svelte/store";

import type { Writable } from "svelte/store";
import type { Point, Tool } from "./types";
import type { Arc, Line } from "./lib/shapes";

type State = {
  image: HTMLImageElement | undefined;
  currentPoints: Point[];
  currentTool: Tool;
  shapes: (Line | Arc)[];
};

export const state: Writable<State> = writable({
  image: undefined,
  currentPoints: [],
  currentTool: "line",
  shapes: [],
});
