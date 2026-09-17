def analyze_hazards(
    detections,
    environmental_data,
    fire_smoke_detections=None
):
    hazards = []

    temperature = environmental_data["temperature"]
    humidity = environmental_data["humidity"]
    wind_speed = environmental_data["wind_speed"]

    temperature_area = environmental_data.get(
        "temperature_area"
    )

    wind_area = environmental_data.get(
        "wind_area"
    )

    humidity_area = environmental_data.get(
        "humidity_area"
    )

    # Human presence
    for detection in detections:
        if detection["object"] == "person":
            hazards.append({
                "type": "person_detected",
                "message": "Possible human presence detected.",
                "severity": "information",
                "confidence": detection["confidence"],
                "location": detection.get("location")
            })

    # High temperature
    if temperature >= 45:
        hazards.append({
            "type": "high_temperature",
            "message": "High temperature detected.",
            "severity": "high",
            "location": temperature_area
        })

    elif temperature >= 38:
        hazards.append({
            "type": "elevated_temperature",
            "message": "Elevated temperature detected.",
            "severity": "moderate",
            "location": temperature_area
        })

    # Strong wind
    if wind_speed >= 40:
        hazards.append({
            "type": "strong_wind",
            "message": "Strong wind conditions detected.",
            "severity": "high",
            "location": wind_area
        })

    elif wind_speed >= 25:
        hazards.append({
            "type": "moderate_wind",
            "message": "Moderate-to-strong wind conditions detected.",
            "severity": "moderate",
            "location": wind_area
        })

    # Low humidity
    if humidity <= 30:
        hazards.append({
            "type": "low_humidity",
            "message": "Low humidity detected.",
            "severity": "moderate",
            "location": humidity_area
        })

    # Fire / smoke
    if fire_smoke_detections:
        for detection in fire_smoke_detections:
            hazards.append({
                "type": detection["type"],
                "message": f"{detection['type'].capitalize()} detected.",
                "severity": "high",
                "confidence": detection["confidence"],
                "location": detection.get("location")
            })

    return hazards


if __name__ == "__main__":
    print("Hazard analysis module initialized.")