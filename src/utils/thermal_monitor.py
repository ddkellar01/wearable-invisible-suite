"""
thermal_monitor.py
Monitors Jetson Orin Nano thermal sensors and triggers protective dimming if needed.
"""

import time
from src.utils.logger import setup_logger

logger = setup_logger("ThermalMonitor")

class ThermalMonitor:
    def __init__(self, max_temp=75.0):
        self.max_temp = max_temp

    def get_current_temperature(self):
        # Simulated reading from sysfs thermal zone
        return 42.5

    def check_thermal_status(self):
        temp = self.get_current_temperature()
        if temp >= self.max_temp:
            logger.warning(f"Thermal threshold exceeded: {temp}°C! Reducing frame rate.")
            return True
        return False
