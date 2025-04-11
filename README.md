# Drone Security Simulation Project

This repository contains scripts and documentation for a project in **Intro to Computer Security**. Our focus is on exploring vulnerabilities in drone communication systems, specifically RF jamming, and evaluating software-based countermeasures such as frequency hopping and automated drone behaviors during signal loss.

---

## Project Overview

**Course:** Intro to Computer Security  
**Team Name:** Phantom Phishers  
**Goal:** Investigate communication-based attacks on delivery drones and evaluate basic defensive strategies using simulation.

We used the multiUAV Gazebo simulation environment:  
https://github.com/monemati/multiuav-gazebo-simulation  
along with **ArduPilot SITL** and **MAVProxy**.

---

## Simulation Environment Setup

To run a single UAV simulation:

**Terminal 1**
```
cd ~/ardupilot/Tools/autotest
./sim_vehicle.py -v ArduCopter -f gazebo-iris --console -I0
```

**Terminal 2**
```
gazebo --verbose ~/ardupilot_gazebo/worlds/iris_ardupilot.world
```

**Then in MAVProxy console:**
```
mode guided
arm throttle
takeoff 5
```

---

## Simulations

### Simulation 1: RF Jamming Attack (No Defense)

This simulation demonstrates what happens when a drone loses communication mid-flight due to a jamming-like event.

[add visuals]

---

### Simulation 2: Frequency Hopping (Defense Script)

This simulation uses a basic frequency hopping script to simulate detection of jamming and a shift to a new communication “channel.”

[add visuals]

---

### Simulation 3: Drone Response to Signal Loss

In this scenario, we configure the drone to detect communication failure and automatically respond by switching flight modes (e.g., LAND).

[add visuals]

---

## Repository Structure

```
scripts/       - Python scripts for jamming, frequency hopping, behavior control  
images/        - Screenshots for documentation and presentation  
README.md      - Project summary and setup instructions
```

---

## Team Members

Tommy Baratta  
Allison Brown  
Andrea Safadi  
Vesper Nguyen  
Zander Picon  

---

## Notes

All experiments were run in a virtual simulation environment using SITL and Gazebo. No real drone hardware was used.  
This project is intended for academic purposes and supports our exploration of secure communication in hybrid drone delivery systems.

