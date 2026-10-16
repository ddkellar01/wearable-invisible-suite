import pytest
import numpy as np
from src.optics.perspective_warp import PerspectiveWarper

def test_perspective_warper():
    src = [[0, 0], [100, 0], [100, 100], [0, 100]]
    dst = [[10, 10], [90, 10], [90, 90], [10, 90]]
    warper = PerspectiveWarper(src, dst)
    assert warper.matrix is not None
