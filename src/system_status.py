def generate_system_status(
    detections,
    environmental_data,
    hazards,
    route,
    fire_smoke_detections=None
):
    status = {
        "vision": "operational",
        "fire_smoke_detection": (
            "operational"
            if fire_smoke_detections is not None
            else "unavailable"
        ),
        "environmental_sensors": (
            "operational"
            if environmental_data
            else "unavailable"
        ),
        "hazard_analysis": "operational",
        "hazard_mapping": "operational",
        "route_analysis": (
            "operational"
            if route
            else "no_route"
        ),
        "hazard_count": len(hazards),
        "detected_object_count": len(detections),
        "fire_smoke_detection_count": (
            len(fire_smoke_detections)
            if fire_smoke_detections is not None
            else 0
        ),
        "environmental_data_available": (
            bool(environmental_data)
        )
    }

    return status


def display_system_status(status):
    print("\nSystem Status:")
    print("-------------")

    print(
        f"- Vision: "
        f"{status['vision']}"
    )

    print(
        f"- Fire / Smoke Detection: "
        f"{status['fire_smoke_detection']}"
    )

    print(
        f"- Environmental Sensors: "
        f"{status['environmental_sensors']}"
    )

    print(
        f"- Hazard Analysis: "
        f"{status['hazard_analysis']}"
    )

    print(
        f"- Hazard Mapping: "
        f"{status['hazard_mapping']}"
    )

    print(
        f"- Route Analysis: "
        f"{status['route_analysis']}"
    )

    print(
        f"- Detected Objects: "
        f"{status['detected_object_count']}"
    )

    print(
        f"- Fire / Smoke Detections: "
        f"{status['fire_smoke_detection_count']}"
    )

    print(
        f"- Hazards Identified: "
        f"{status['hazard_count']}"
    )

    if status["environmental_data_available"]:
        print(
            "- Environmental Data: available"
        )
    else:
        print(
            "- Environmental Data: unavailable"
        )


if __name__ == "__main__":
    example_status = generate_system_status(
        detections=[],
        environmental_data={
            "temperature": 30,
            "humidity": 50,
            "wind_speed": 10,
            "wind_direction": "N"
        },
        hazards=[],
        route=[(0, 0), (0, 1)],
        fire_smoke_detections=[]
    )

    display_system_status(
        example_status
    )