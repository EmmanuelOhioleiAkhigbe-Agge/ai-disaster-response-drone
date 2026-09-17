from PIL import Image


def detect_fire_smoke(image_path):
    """
    Lightweight fire and smoke detection.

    This V1 detector uses image-color characteristics
    to identify regions that may contain fire or smoke.

    It is a research prototype and does not replace
    a trained fire/smoke detection model.

    Detection format:

    {
        "type": "fire" or "smoke",
        "confidence": value,
        "location": {
            "x": normalized_x,
            "y": normalized_y
        }
    }
    """

    image = Image.open(image_path).convert("RGB")

    width, height = image.size
    pixels = image.load()

    fire_pixels = []
    smoke_pixels = []

    for y in range(height):
        for x in range(width):
            red, green, blue = pixels[x, y]

            # Basic flame-color heuristic.
            if (
                red > 180
                and green > 70
                and green < 210
                and blue < 100
                and red > green * 1.15
            ):
                fire_pixels.append((x, y))

            # Basic smoke-color heuristic.
            brightness = (
                red + green + blue
            ) / 3

            color_difference = max(
                red, green, blue
            ) - min(
                red, green, blue
            )

            if (
                60 <= brightness <= 210
                and color_difference <= 25
            ):
                smoke_pixels.append((x, y))

    detections = []

    # Fire detection
    if fire_pixels:
        average_x = sum(
            pixel[0] for pixel in fire_pixels
        ) / len(fire_pixels)

        average_y = sum(
            pixel[1] for pixel in fire_pixels
        ) / len(fire_pixels)

        fire_area = (
            len(fire_pixels)
            / (width * height)
        )

        confidence = min(
            0.95,
            0.50 + fire_area * 10
        )

        detections.append({
            "type": "fire",
            "confidence": round(confidence, 2),
            "location": {
                "x": round(
                    average_x / width,
                    3
                ),
                "y": round(
                    average_y / height,
                    3
                )
            }
        })

    # Smoke detection
    if smoke_pixels:
        average_x = sum(
            pixel[0] for pixel in smoke_pixels
        ) / len(smoke_pixels)

        average_y = sum(
            pixel[1] for pixel in smoke_pixels
        ) / len(smoke_pixels)

        smoke_area = (
            len(smoke_pixels)
            / (width * height)
        )

        confidence = min(
            0.90,
            0.40 + smoke_area * 5
        )

        detections.append({
            "type": "smoke",
            "confidence": round(confidence, 2),
            "location": {
                "x": round(
                    average_x / width,
                    3
                ),
                "y": round(
                    average_y / height,
                    3
                )
            }
        })

    return detections


if __name__ == "__main__":
    image_path = "data/fire.688.webp"

    results = detect_fire_smoke(
        image_path
    )

    print("Fire / Smoke Detection")
    print("----------------------")

    if results:
        for result in results:
            print(
                f"Detected: {result['type']} "
                f"| Confidence: "
                f"{result['confidence']}"
            )

            print(
                f"Location: "
                f"x={result['location']['x']}, "
                f"y={result['location']['y']}"
            )
    else:
        print(
            "No fire or smoke detected."
        )