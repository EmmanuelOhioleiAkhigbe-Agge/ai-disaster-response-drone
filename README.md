# AI-Assisted Disaster Response Drone

A Python-based research prototype for AI-assisted disaster situational awareness and responder decision support.

The system combines visual analysis, environmental information, fire/smoke detection, hazard analysis, spatial mapping, route analysis, and responder-oriented reporting into a single prototype pipeline.

The core design principle is **human-AI collaboration**: the system provides observations, estimated hazards, possible routes, and confidence information while trained human responders retain decision-making authority.

---

## Overview

During disasters, responders may have incomplete or rapidly changing information about their surroundings.

This project explores how an AI-assisted drone system could help provide additional situational awareness by combining information from multiple sources.

The current prototype demonstrates a simplified version of this concept using:

* Image-based object detection
* Fire and smoke detection
* Simulated environmental sensor data
* Sensor fusion
* Hazard analysis
* Adaptive hazard mapping
* Route analysis
* Confidence reporting
* Human-facing situation reports

The current implementation is a research prototype and does **not** represent a production-ready autonomous disaster-response system.

---

## System Architecture

The current processing pipeline is:

```text
                    Input Image
                         |
                         v
              +---------------------+
              |  Object Detection   |
              |       YOLO           |
              +----------+----------+
                         |
                         v
              +---------------------+
              | Fire / Smoke        |
              | Detection            |
              +----------+----------+
                         |
                         v
              +---------------------+
              | Environmental Data  |
              | Temperature         |
              | Humidity             |
              | Wind                 |
              +----------+----------+
                         |
                         v
              +---------------------+
              |   Sensor Fusion      |
              +----------+----------+
                         |
                         v
              +---------------------+
              |  Hazard Analysis     |
              +----------+----------+
                         |
                         v
              +---------------------+
              | Adaptive Hazard Map  |
              +----------+----------+
                         |
                         v
              +---------------------+
              |   Route Analysis     |
              +----------+----------+
                         |
                         v
              +---------------------+
              | Responder Report     |
              | + System Status      |
              +---------------------+
```

---

## Current Features

### 1. Visual Object Detection

The system uses a lightweight YOLO model through the Ultralytics framework to identify objects in an input image.

The current prototype records:

* Object class
* Detection confidence
* Normalized location
* Bounding box coordinates

Example:

```text
Detected: person
Confidence: 0.86
Location: x=0.567, y=0.548
```

The system treats detected people as observations rather than automatically classifying them as hazards.

---

### 2. Fire and Smoke Detection

The prototype contains a lightweight image-based fire/smoke detector.

The current V1 implementation uses image-color characteristics to identify regions that may contain:

* Fire
* Smoke

Each detection includes:

* Detection type
* Heuristic confidence value
* Normalized image location

Example:

```text
fire
confidence: 0.95
location: x=0.491, y=0.500
```

The current detector is intentionally lightweight and should be considered experimental.

It is **not a validated fire or smoke recognition model**.

---

### 3. Environmental Data

The prototype currently uses simulated environmental information representing potential drone sensor inputs.

The current data includes:

* Temperature
* Humidity
* Wind speed
* Wind direction

Example:

```text
Temperature: 48.0 °C
Humidity: 25.0 %
Wind Speed: 50.0 km/h
Wind Direction: E
```

Some environmental locations are also simulated so that the prototype can demonstrate spatial hazard analysis.

Future versions can replace these simulated values with real drone-mounted sensors.

---

### 4. Sensor Fusion

The sensor-fusion layer combines information from different system components into a common situation snapshot.

The snapshot currently contains:

```text
Detected objects
Environmental conditions
Hazards
Fire / smoke detections
```

This provides the foundation for combining multiple sensor sources rather than analyzing every sensor independently.

---

### 5. Hazard Analysis

The hazard-analysis component evaluates information from the available sources.

Current examples include:

* Human presence
* High temperature
* Elevated temperature
* Strong wind
* Moderate wind
* Low humidity
* Fire
* Smoke

Hazards are assigned descriptive severity levels where appropriate.

A detected person is represented as an informational observation rather than automatically being treated as a dangerous obstacle.

---

### 6. Adaptive Hazard Mapping

The system converts available hazard and detection information into a simplified spatial grid.

The current map uses:

```text
F = Fire
S = Smoke
H = Detected obstacle
* = Possible route
# = Hazard / blocked area
. = Open area
```

Example:

```text
* . # . .
* # # # .
* S F # .
* # # . .
* * * * *
```

The map is designed to change according to the information supplied to the system rather than being purely decorative.

The current spatial representation is still a simplified prototype grid and is not a real geographic map.

---

### 7. Route Analysis

The system uses grid-based pathfinding to identify a possible route through areas that are not currently marked as hazardous or blocked.

The current implementation uses breadth-first search.

A route is described as a **possible route** rather than a guaranteed safe route.

Example:

```text
Possible route identified.

(0, 0)
(1, 0)
(2, 0)
(3, 0)
(4, 0)
(4, 1)
(4, 2)
(4, 3)
(4, 4)
```

The system can recalculate the route when the hazard grid changes.

---

### 8. Responder Situation Report

The responder-report component converts the system's internal data into a human-readable report.

The report can include:

* Detected objects
* Object locations
* Environmental conditions
* Fire/smoke detections
* Hazard severity
* Hazard locations
* Route information
* Confidence summary
* Human decision notice

The goal is to provide concise information that could assist trained responders rather than replacing their judgment.

---

### 9. System Status

The system also reports the operational state of its major components.

Example:

```text
System Status:
-------------
- Vision: operational
- Fire / Smoke Detection: operational
- Environmental Sensors: operational
- Hazard Analysis: operational
- Hazard Mapping: operational
- Route Analysis: operational
```

This provides a basic foundation for monitoring the state of the prototype's processing pipeline.

---

## Project Structure

```text
ai-disaster-response-drone/
│
├── data/
│   ├── Mountain.986.jpg
│   ├── person.977.webp
│   └── fire.688.webp
│
├── src/
│   ├── main.py
│   ├── environmental_data.py
│   ├── hazard_analysis.py
│   ├── fire_smoke_detection.py
│   ├── sensor_fusion.py
│   ├── route_analysis.py
│   ├── responder_report.py
│   ├── situation_map.py
│   ├── hazard_map.py
│   ├── system_status.py
│   │
│   └── vision/
│       └── object_detection.py
│
└── README.md
```

---

## Running the Prototype

From the project root:

```bash
python src/main.py
```

The default test image is:

```text
data/fire.688.webp
```

A different image can be supplied without modifying the source code:

```bash
python src/main.py data/person.977.webp
```

This allows different test images to be used as simulated drone-camera input.

---

## Technologies

* Python
* YOLO / Ultralytics
* Pillow
* Computer vision
* Rule-based hazard analysis
* Grid-based pathfinding
* Sensor-fusion concepts
* Windows development environment
* Git / GitHub

---

## Current Prototype Limitations

This project is intentionally a research prototype.

### Simulated environmental sensors

Temperature, humidity, wind speed, wind direction, and some spatial influence areas are currently simulated.

They do not represent live drone sensor measurements.

### Experimental fire/smoke detector

The current fire/smoke detector uses simple image-color heuristics.

It can produce false positives or false negatives.

For example, an image without an actual smoke source may still contain colors that satisfy the heuristic.

A future version should use a properly trained and evaluated fire/smoke detection model.

### Simplified spatial representation

The hazard map currently uses a small grid rather than GPS coordinates or a real geographic map.

### Simplified route analysis

The current route system treats hazardous cells as blocked.

Real disaster environments are more complex because hazards can have different levels of risk and may change continuously.

### No autonomous drone control

The prototype does not control a drone.

It does not:

* Pilot a drone
* Select flight paths autonomously
* Control firefighting equipment
* Make rescue decisions
* Control helicopters
* Deploy emergency equipment

### No real disaster prediction

The current system does not reliably predict earthquakes, wildfires, tsunamis, structural collapse, or other disasters.

Future research may investigate early-warning and predictive models, but such capabilities would require substantial real-world datasets and validation.

---

## Human-AI Decision Model

A central design principle of this project is that AI should function as a **decision-support system**, not an autonomous authority.

The system is intended to:

```text
Observe
   ↓
Analyze
   ↓
Estimate
   ↓
Explain
   ↓
Present options
   ↓
Human decision
```

Rather than:

```text
Observe
   ↓
AI decides
   ↓
AI acts
```

For example, the system may identify a possible route around detected hazards.

It does not claim that the route is guaranteed safe, and it does not decide whether a responder should enter that route.

The final decision remains with trained personnel who can consider information unavailable to the AI.

---

## Research Direction

The current prototype provides a foundation for future work involving more advanced multimodal sensing.

Potential future sensor sources include:

* RGB cameras
* Thermal cameras
* LiDAR
* Radar
* Depth sensors
* Environmental sensors
* GPS
* Inertial measurement systems
* Other drone telemetry

Combining these sources could provide a richer representation of disaster environments.

Future research could investigate how multimodal sensor fusion can improve:

* Hazard localization
* Structural-risk assessment
* Fire and smoke analysis
* Human detection
* Route assessment
* Dynamic hazard updates
* Situational awareness

---

## Future Development

Possible future versions may include:

* Real-time drone video
* Real environmental sensors
* GPS-based mapping
* Thermal imaging
* LiDAR-based environmental reconstruction
* Improved fire/smoke detection
* Risk-aware rather than binary route planning
* Dynamic route reassessment
* Structural damage analysis
* Human detection and tracking
* Multi-drone cooperation
* Responder-worn sensor integration
* Real-time communication
* Lightweight machine-learning anomaly detection
* Confidence calibration and evaluation
* Historical event analysis
* More advanced sensor-fusion models

These features would be developed incrementally and evaluated independently.

---

## Research and Educational Purpose

This project is intended to explore concepts in:

* Artificial intelligence
* Computer vision
* Cyber-physical systems
* Sensor fusion
* Disaster-response technology
* Decision-support systems
* Human-AI collaboration
* Autonomous-systems research

The emphasis is on understanding how AI can provide useful situational information while keeping critical decisions under human control.

---

## Disclaimer

This project is an educational and research prototype.

It has not been validated for operational emergency response and should not be relied upon for real-world rescue, firefighting, navigation, or life-critical decisions.

All real-world deployment would require appropriate testing, validation, safety engineering, regulatory compliance, and qualified human supervision.
