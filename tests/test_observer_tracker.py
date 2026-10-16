import pytest
import numpy as np
from src.observer_tracker import ObserverTracker

def test_observer_tracker():
    tracker = ObserverTracker()
    vector = tracker.estimate_observer_angle(None)
    assert isinstance(vector, np.ndarray)
    assert vector.shape == (3,)
