def create_situation_snapshot(
    detections,
    environmental_data,
    hazards,
    fire_smoke_detections
):
    snapshot = {
        "detected_objects": detections,
        "environment": environmental_data,
        "hazards": hazards,
        "fire_smoke": fire_smoke_detections
    }

    return snapshot


if __name__ == "__main__":
    print("Sensor fusion module initialized.")