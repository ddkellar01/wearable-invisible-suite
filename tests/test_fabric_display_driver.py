import pytest
import numpy as np
from src.optics.fabric_display_driver import FabricDisplayDriver

def test_display_driver_formatting():
    driver = FabricDisplayDriver(panel_resolution=(100, 100))
    dummy_frame = np.zeros((200, 200, 3), dtype=np.uint8)
    formatted = driver.format_frame_for_weave(dummy_frame)
    assert formatted.shape == (100, 100, 3)
