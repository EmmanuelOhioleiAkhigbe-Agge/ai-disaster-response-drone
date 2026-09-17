def calculate_overall_confidence(situation):
    confidence_values = []

    for detection in situation["detected_objects"]:
        if "confidence" in detection:
            confidence_values.append(
                detection["confidence"]
            )

    for detection in situation["fire_smoke"]:
        if "confidence" in detection:
            confidence_values.append(
                detection["confidence"]
            )

    if not confidence_values:
        return None

    average_confidence = (
        sum(confidence_values)
        / len(confidence_values)
    )

    return round(
        average_confidence,
        2
    )


def format_location(location):
    if not location:
        return None

    if isinstance(location, dict):
        x = location.get("x")
        y = location.get("y")

        if x is not None and y is not None:
            return f"x={x}, y={y}"

    if isinstance(location, (tuple, list)):
        if len(location) == 2:
            return f"map cell={tuple(location)}"

    return None


def generate_responder_report(
    situation,
    route=None
):
    report = []

    report.append(
        "DISASTER RESPONSE SITUATION REPORT"
    )
    report.append(
        "----------------------------------"
    )

    # Detected objects
    report.append("\nDetected Objects:")

    objects = situation["detected_objects"]

    if objects:
        for detection in objects:
            message = (
                f"- {detection['object']} "
                f"(confidence: "
                f"{detection['confidence']})"
            )

            location = format_location(
                detection.get("location")
            )

            if location:
                message += (
                    f" | Location: {location}"
                )

            report.append(message)
    else:
        report.append(
            "- No objects detected."
        )

    # Environmental conditions
    environment = situation["environment"]

    report.append(
        "\nEnvironmental Conditions:"
    )

    report.append(
        f"- Temperature: "
        f"{environment['temperature']} °C"
    )

    report.append(
        f"- Humidity: "
        f"{environment['humidity']} %"
    )

    report.append(
        f"- Wind Speed: "
        f"{environment['wind_speed']} km/h"
    )

    report.append(
        f"- Wind Direction: "
        f"{environment['wind_direction']}"
    )

    # Fire and smoke
    report.append("\nFire / Smoke:")

    fire_smoke = situation["fire_smoke"]

    if fire_smoke:
        for detection in fire_smoke:
            message = (
                f"- {detection['type']} "
                f"(confidence: "
                f"{detection['confidence']})"
            )

            location = format_location(
                detection.get("location")
            )

            if location:
                message += (
                    f" | Location: {location}"
                )

            report.append(message)
    else:
        report.append(
            "- No fire or smoke detected."
        )

    # Hazards
    report.append("\nHazards:")

    hazards = situation["hazards"]

    if hazards:
        for hazard in hazards:
            message = (
                f"- {hazard['message']}"
            )

            if "severity" in hazard:
                message += (
                    f" | Severity: "
                    f"{hazard['severity']}"
                )

            if "confidence" in hazard:
                message += (
                    f" | Confidence: "
                    f"{hazard['confidence']}"
                )

            location = format_location(
                hazard.get("location")
            )

            if location:
                message += (
                    f" | Location: {location}"
                )

            report.append(message)

    else:
        report.append(
            "- No immediate hazards detected."
        )

    # Route
    report.append("\nRoute Analysis:")

    if route:
        report.append(
            "- Possible route identified."
        )

        for position in route:
            report.append(
                f"  {position}"
            )
    else:
        report.append(
            "- No route available."
        )

    # Confidence summary
    overall_confidence = (
        calculate_overall_confidence(
            situation
        )
    )

    report.append(
        "\nConfidence Summary:"
    )

    if overall_confidence is not None:
        report.append(
            f"- Average detection confidence: "
            f"{overall_confidence}"
        )
    else:
        report.append(
            "- No confidence score available."
        )

    # Human authority
    report.append(
        "\nHuman Decision Required:"
    )

    report.append(
        "- AI provides observations and "
        "route information."
    )

    report.append(
        "- Confidence values indicate model "
        "or heuristic certainty, not guaranteed "
        "real-world accuracy."
    )

    report.append(
        "- Environmental measurements and "
        "hazard locations may be simulated "
        "in the current prototype."
    )

    report.append(
        "- Trained responders retain "
        "decision-making authority."
    )

    return "\n".join(report)


if __name__ == "__main__":
    print(
        "Responder report module initialized."
    )