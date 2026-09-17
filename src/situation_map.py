def display_situation_map(
    grid,
    route=None,
    detections=None,
    fire_smoke_detections=None
):
    print("\nSituation Map:")
    print("-------------")

    route_positions = set(route or [])

    hazard_positions = set()

    # Convert normal detections into map positions.
    if detections:
        for detection in detections:
            location = detection.get("location")

            if not isinstance(location, dict):
                continue

            x = location.get("x")
            y = location.get("y")

            if x is None or y is None:
                continue

            row = min(
                int(y * len(grid)),
                len(grid) - 1
            )

            col = min(
                int(x * len(grid[0])),
                len(grid[0]) - 1
            )

            object_type = detection.get(
                "object"
            )

            if object_type != "person":
                hazard_positions.add(
                    (row, col)
                )

    # Convert fire/smoke detections into map positions.
    fire_positions = set()
    smoke_positions = set()

    if fire_smoke_detections:
        for detection in fire_smoke_detections:
            location = detection.get("location")

            if not isinstance(location, dict):
                continue

            x = location.get("x")
            y = location.get("y")

            if x is None or y is None:
                continue

            row = min(
                int(y * len(grid)),
                len(grid) - 1
            )

            col = min(
                int(x * len(grid[0])),
                len(grid[0]) - 1
            )

            if detection.get("type") == "fire":
                fire_positions.add(
                    (row, col)
                )

            elif detection.get("type") == "smoke":
                smoke_positions.add(
                    (row, col)
                )

    for row_index, row in enumerate(grid):
        line = ""

        for col_index, cell in enumerate(row):
            position = (
                row_index,
                col_index
            )

            if position in fire_positions:
                line += "F "

            elif position in smoke_positions:
                line += "S "

            elif position in hazard_positions:
                line += "H "

            elif position in route_positions:
                line += "* "

            elif cell == 1:
                line += "# "

            else:
                line += ". "

        print(line)

    print("\nLegend:")
    print("F = Fire detected")
    print("S = Smoke detected")
    print("H = Detected obstacle")
    print("* = Possible route")
    print("# = Hazard / blocked area")
    print(". = Open area")


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    route = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 2),
        (3, 3),
        (3, 4),
        (4, 4)
    ]

    detections = [
        {
            "object": "person",
            "confidence": 0.86,
            "location": {
                "x": 0.52,
                "y": 0.61
            }
        }
    ]

    fire_smoke_detections = [
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

    display_situation_map(
        grid,
        route,
        detections,
        fire_smoke_detections
    )