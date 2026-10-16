"""
config_loader.py
Loads configuration parameters for camera arrays, display panels, and system thresholds.
"""

import os

class ConfigLoader:
    @staticmethod
    def load_default_config():
        return {
            "target_fps": 60,
            "camera_resolution": [3840, 2160],
            "display_resolution": [1920, 1080],
            "max_temp_threshold_c": 75.0
        }
