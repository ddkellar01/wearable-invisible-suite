"""
imu_calibrator.py
Performs zero-bias calibration for the embedded IMU body mesh sensors.
"""

import numpy as np

def calibrate_imus(sensor_samples):
    print("Calculating IMU gyroscope and accelerometer offsets...")
    offsets = np.mean(sensor_samples, axis=0)
    return offsets

if __name__ == "__main__":
    dummy_data = np.random.normal(0, 0.01, (100, 4))
    print("Calculated offsets:", calibrate_imus(dummy_data))
