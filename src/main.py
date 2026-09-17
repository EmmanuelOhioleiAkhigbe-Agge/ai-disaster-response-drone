import sys

from vision.object_detection import detect_objects
from environmental_data import get_environmental_data
from hazard_analysis import analyze_hazards
from fire_smoke_detection import detect_fire_smoke
from sensor_fusion import create_situation_snapshot
from route_analysis import reassess_route
from responder_report import generate_responder_report
from situation_map import display_situation_map
from hazard_map import create_hazard_grid
from system_status import (
    generate_system_status,
    display_system_status
)


def main():
    print(
        "AI-Assisted Disaster Response Drone"
    )
    print(
        "-----------------------------------"
    )

    # Use an image supplied from the command line.
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = "data/fire.688.webp"

    print(
        f"Input Image: {image_path}"
    )

    # 1. Visual object detection
    detections = detect_objects(
        image_path
    )

    # 2. Environmental data
    environmental_data = (
        get_environmental_data()
    )

    # 3. Fire and smoke detection
    fire_smoke_detections = (
        detect_fire_smoke(
            image_path
        )
    )

    # 4. Hazard analysis
    hazards = analyze_hazards(
        detections,
        environmental_data,
        fire_smoke_detections
    )

    # 5. Sensor fusion
    situation = create_situation_snapshot(
        detections,
        environmental_data,
        hazards,
        fire_smoke_detections
    )

    # 6. Combine spatial detections.
    spatial_detections = (
        detections
        + fire_smoke_detections
    )

    # 7. Generate adaptive hazard map.
    grid = create_hazard_grid(
        hazards=hazards,
        detections=spatial_detections
    )

    start = (0, 0)
    goal = (4, 4)

    # 8. Reassess route.
    route_result = reassess_route(
        grid,
        start,
        goal
    )

    route = route_result["route"]

    # 9. Display situation map.
    display_situation_map(
        grid,
        route,
        detections,
        fire_smoke_detections
    )

    # 10. Generate responder report.
    report = generate_responder_report(
        situation,
        route
    )

    # 11. Generate system status.
    status = generate_system_status(
        detections,
        environmental_data,
        hazards,
        route,
        fire_smoke_detections
    )

    # 12. Display system status.
    display_system_status(
        status
    )

    # 13. Display route status.
    print("\nRoute Status:")

    if route_result["status"] == "route_available":
        print(
            "- Possible route currently available."
        )
    else:
        print(
            "- No route currently available."
        )

    # 14. Display final report.
    print("\n")
    print(report)


if __name__ == "__main__":
    main()