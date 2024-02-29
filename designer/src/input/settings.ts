import type { Dimensions } from "../types";

type Settings = {
  target: string;
  real: Dimensions;
  photo: Dimensions;
};

const SETTINGS: Settings = {
  target: "/target.png",
  real: {
    width: 140,
    height: 80,
  },
  photo: {
    width: 2201,
    height: 3825,
  },
};

export default SETTINGS;
