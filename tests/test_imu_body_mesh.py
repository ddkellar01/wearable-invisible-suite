import pytest
from src.imu_body_mesh import IMUBodyMeshTracker

def test_imu_tracker():
    tracker = IMUBodyMeshTracker(sensor_count=4)
    data = tracker.read_imu_data()
    assert data.shape == (4, 4)
