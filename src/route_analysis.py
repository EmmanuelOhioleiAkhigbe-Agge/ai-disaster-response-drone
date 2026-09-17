from collections import deque


def find_route(grid, start, goal):
    """
    Find a possible route through a grid while avoiding
    hazardous or blocked areas.

    0 = open area
    1 = hazardous/blocked area
    """

    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    visited = {start}
    previous = {}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        current = queue.popleft()

        if current == goal:
            route = []
            position = goal

            while position != start:
                route.append(position)
                position = previous[position]

            route.append(start)
            route.reverse()

            return route

        for row_change, col_change in directions:
            next_position = (
                current[0] + row_change,
                current[1] + col_change
            )

            row, col = next_position

            if not (0 <= row < rows and 0 <= col < cols):
                continue

            if grid[row][col] == 1:
                continue

            if next_position in visited:
                continue

            visited.add(next_position)
            previous[next_position] = current
            queue.append(next_position)

    return None


def reassess_route(grid, start, goal):
    """
    Recalculate the route using the latest hazard map.
    """

    route = find_route(
        grid,
        start,
        goal
    )

    if route:
        return {
            "status": "route_available",
            "route": route
        }

    return {
        "status": "no_route_available",
        "route": []
    }


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    result = reassess_route(
        grid,
        start,
        goal
    )

    if result["status"] == "route_available":
        print("Route available.")

        for position in result["route"]:
            print(f"- {position}")
    else:
        print("No route currently available.")