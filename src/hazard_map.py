def create_hazard_grid(
    hazards=None,
    detections=None,
    rows=5,
    cols=5
):
    """
    Create an adaptive hazard map.

    0 = open area
    1 = hazardous / blocked area

    Grid-based hazard locations use:
        "location": (row, column)

    Vision and fire/smoke detections use normalized
    coordinates:
        "location": {
            "x": 0.0 to 1.0,
            "y": 0.0 to 1.0
        }
    """

    grid = [
        [0 for _ in range(cols)]
        for _ in range(rows)
    ]

    # Base simulated structural hazards.
    base_hazards = [
        {
            "type": "structural_hazard",
            "severity": "high",
            "location": (1, 1)
        },
        {
            "type": "structural_hazard",
            "severity": "high",
            "location": (1, 2)
        },
        {
            "type": "structural_hazard",
            "severity": "high",
            "location": (1, 3)
        },
        {
            "type": "structural_hazard",
            "severity": "high",
            "location": (2, 3)
        },
        {
            "type": "structural_hazard",
            "severity": "high",
            "location": (3, 1)
        }
    ]

    all_hazards = base_hazards.copy()

    if hazards:
        all_hazards.extend(hazards)

    # Add hazards with explicit grid coordinates.
    for hazard in all_hazards:
        location = hazard.get("location")

        if not isinstance(location, (tuple, list)):
            continue

        if len(location) != 2:
            continue

        row, col = location

        if not isinstance(row, int) or not isinstance(col, int):
            continue

        if 0 <= row < rows and 0 <= col < cols:
            grid[row][col] = 1

    # Add vision and fire/smoke detections.
    if detections:
        for detection in detections:
            location = detection.get("location")

            if not isinstance(location, dict):
                continue

            x = location.get("x")
            y = location.get("y")

            if x is None or y is None:
                continue

            if not (0.0 <= x <= 1.0):
                continue

            if not (0.0 <= y <= 1.0):
                continue

            col = min(
                int(x * cols),
                cols - 1
            )

            row = min(
                int(y * rows),
                rows - 1
            )

            object_type = detection.get(
                "object"
            )

            detection_type = detection.get(
                "type"
            )

            # People are observations, not automatically hazards.
            if object_type == "person":
                continue

            # Fire and smoke are treated as hazards.
            if detection_type in (
                "fire",
                "smoke"
            ):
                grid[row][col] = 1

            # Other detected objects can also be
            # represented as obstacles when appropriate.
            elif object_type in (
                "car",
                "truck",
                "bus",
                "motorcycle"
            ):
                grid[row][col] = 1

    return grid


if __name__ == "__main__":
    example_hazards = [
        {
            "type": "strong_wind",
            "severity": "high",
            "location": (0, 2)
        },
        {
            "type": "high_temperature",
            "severity": "high",
            "location": (2, 2)
        }
    ]

    example_detections = [
        {
            "object": "person",
            "confidence": 0.86,
            "location": {
                "x": 0.52,
                "y": 0.61
            }
        },
        {
            "type": "fire",
            "confidence": 0.95,
            "location": {
                "x": 0.491,
                "y": 0.5
            }
        },
        {
            "type": "smoke",
            "confidence": 0.57,
            "location": {
                "x": 0.333,
                "y": 0.504
            }
        }
    ]

    grid = create_hazard_grid(
        hazards=example_hazards,
        detections=example_detections
    )

    print("Adaptive Hazard Grid:")
    print("---------------------")

    for row in grid:
        print(row)