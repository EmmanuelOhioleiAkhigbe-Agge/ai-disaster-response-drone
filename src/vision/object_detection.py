from ultralytics import YOLO


model = YOLO("yolo11n.pt")


def detect_objects(image_path):
    results = model(image_path)
    detections = []

    for result in results:
        image_height, image_width = result.orig_shape

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            name = model.names[class_id]

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            normalized_x = center_x / image_width
            normalized_y = center_y / image_height

            detection = {
                "object": name,
                "confidence": round(confidence, 2),
                "location": {
                    "x": round(normalized_x, 3),
                    "y": round(normalized_y, 3)
                },
                "bounding_box": {
                    "x1": round(x1, 1),
                    "y1": round(y1, 1),
                    "x2": round(x2, 1),
                    "y2": round(y2, 1)
                }
            }

            detections.append(detection)

    return detections


if __name__ == "__main__":
    detections = detect_objects("data/person.977.webp")

    for detection in detections:
        print(
            f"Detected: {detection['object']} | "
            f"Confidence: {detection['confidence']}"
        )

        print(
            f"Location: "
            f"x={detection['location']['x']}, "
            f"y={detection['location']['y']}"
        )

        print(
            f"Bounding Box: "
            f"{detection['bounding_box']}"
        )