import pytest
from src.optics.camera_stitching import CameraStitcher

def test_stitcher_initialization():
    stitcher = CameraStitcher([])
    assert stitcher.camera_ids == []
