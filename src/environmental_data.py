def get_environmental_data():
    environmental_data = {
        "temperature": 48.0,
        "humidity": 25.0,
        "wind_speed": 50.0,
        "wind_direction": "E",

        # Simulated environmental influence areas.
        # These represent areas affected by the environmental
        # conditions in the current test scenario.
        "temperature_area": (2, 2),
        "wind_area": (0, 2),
        "humidity_area": (3, 2)
    }

    return environmental_data


if __name__ == "__main__":
    data = get_environmental_data()

    print("Environmental Data")
    print("------------------")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Humidity: {data['humidity']} %")
    print(f"Wind Speed: {data['wind_speed']} km/h")
    print(f"Wind Direction: {data['wind_direction']}")

    print("\nSimulated Influence Areas:")
    print(
        f"Temperature Area: "
        f"{data['temperature_area']}"
    )
    print(
        f"Wind Area: "
        f"{data['wind_area']}"
    )
    print(
        f"Humidity Area: "
        f"{data['humidity_area']}"
    )