# Wearable Invisible Body Motion Suite (Active Camouflage Edition)

An open-source hardware and software framework for an advanced optical camouflage suit featuring real-time perspective warping, flexible OLED/e-paper fabric integration, and low-latency joint telemetry.

---

## 🧰 Tech Stack & Badges

[![Docker Build & Publish](https://github.com/ddkellar01/wearable-invisible-suite/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/ddkellar01/wearable-invisible-suite/actions/workflows/docker-publish.yml)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green.svg)](https://opencv.org/)
[![NVIDIA Jetson Orin Nano](https://img.shields.io/badge/Hardware-Jetson_Orin_Nano-76B900.svg)](https://www.nvidia.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🏛️ What Is This About?

Imagine wearing a superpower suit that makes you look invisible! 🦸‍♂️✨ 

This project is an open-source active optical camouflage suit. It uses tiny micro-cameras mounted around your body to capture what's behind you, and flexible micro-OLED display panels on the front to project that background image in real time—making observers see right through you!

---

## 🚀 Key Features

* **Real-Time Invisibility:** Captures live background views and wraps them across wearable display fabrics instantly.
* **Perspective Warping:** Automatically calculates spatial distortion so background alignment remains accurate even as your body moves.
* **Edge Compute Ready:** Powered locally on the NVIDIA Jetson Orin Nano (ARM64) for mobile, low-power processing.
* **Dockerized CI/CD:** Fully containerized setup for rapid deployment and automated GitHub Actions builds.

---

## ⚙️ How It Works (5th Grade Edition)

Imagine standing in front of a brick wall 🧱 and wanting to hide:

1. 📸 **The Cameras (Eyes):** Tiny cameras on your back take live video of the brick wall behind you.
2. 🧠 **The Computer (Brain):** A mini computer (Jetson Orin Nano) processes those pictures and bends them to fit your body's shape.
3. 🎨 **The Screens (Magic Fabric):** Flexible OLED screens on your suit project the brick wall picture. Anyone looking at you from the front sees the brick wall behind you! 🪄

```text
 🧱 [ Brick Wall ] 
        │
        ▼ (Captured by micro-cameras)
 📸 [ Micro-Camera Array ] 
        │
        ▼ (Sent to Jetson Orin Nano)
 🧠 [ NVIDIA Jetson Brain ] ──(Perspective Warping)──> 🎨 [ Flexible OLED Screens ] ➡️ 🧱 (Invisibility Achieved!)

wearable-invisible-suite/
├── .github/
│   └── workflows/
│       └── docker-publish.yml     # GitHub Actions CI/CD pipeline
├── config/
│   └── default_config.yaml        # Hardware & display matrix configurations
├── docker/
│   ├── Dockerfile                 # PyTorch CUDA container build recipe
│   └── docker-compose.yml         # Multi-service container orchestration
├── hardware/
│   └── cad/                       # 3D printable camera mounts & housing
├── src/
│   ├── calibration/               # Camera and IMU calibration tools
│   ├── optics/                    # Perspective warping & display drivers
│   └── main.py                    # Core execution pipeline
├── requirements.txt               # Python package dependencies
├── update.sh                      # Deployment automation script
└── README.md                      # Repository documentation
