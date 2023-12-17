# Raspberry Pi Breathalyzer Project

This project uses a Raspberry Pi, an MQ 3 sensor, and an LED to create a simple breathalyzer system. The LED continuously glows under normal conditions, but it blinks if alcohol is detected in the user's breath.

## Table of Contents
- [Hardware Requirements](#hardware-requirements)
- [Software Setup](#software-setup)
- [Usage](#usage)
- [Adjusting Sensitivity](#adjusting-sensitivity)
- [Contributing](#contributing)
- [License](#license)

## Hardware Requirements
1. Raspberry Pi (any model with GPIO pins)
2. MQ-3 Sensor 
3. LED
4. Resistor (around 220Ω)
5. Jumper wires

## Software Setup
1. Enable GPIO on the Raspberry Pi.
2. Install the necessary Python library for GPIO interaction:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-rpi.gpio
    ```
3. Download the breathalyzer Python script.

## Usage
1. Run "python breathalyzer.py"
