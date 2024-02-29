import SETTINGS from "../input/settings";

export function getImage(): Promise<HTMLImageElement> {
  return new Promise((resolve, reject) => {
    const image = new Image();

    image.src = SETTINGS.target;

    image.onload = () => resolve(image);
    image.onerror = () =>
      reject(
        `Failed to load the image. Is "${SETTINGS.target}" a valid image? `
      );
  });
}
