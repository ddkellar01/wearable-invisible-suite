"""
main.py
Main entry point integrating all active camouflage subsystems on the Jetson Orin Nano.
"""

import time
from optics.camera_stitching import CameraStitcher
from optics.perspective_warp import PerspectiveWarper
from optics.fabric_display_driver import FabricDisplayDriver
from imu_body_mesh import IMUBodyMeshTracker
from observer_tracker import ObserverTracker

def main():
    print("Initializing Wearable Invisible Body Motion Suite...")
    stitcher = CameraStitcher([0, 1, 2, 3, 4, 5, 6, 7])
    warper = PerspectiveWarper([[0,0],[1920,0],[1920,1080],[0,1080]], [[0,0],[1920,0],[1920,1080],[0,1080]])
    driver = FabricDisplayDriver()
    imu_tracker = IMUBodyMeshTracker()
    observer = ObserverTracker()

    try:
        while True:
            frames = stitcher.capture_frames()
            if frames:
                stitched = stitcher.stitch_feed(frames)
                warped = warper.apply_warp(stitched)
                display_buffer = driver.format_frame_for_weave(warped)
                driver.push_to_panels(display_buffer)
            time.sleep(0.016)  # ~60 FPS target
    except KeyboardInterrupt:
        print("Shutting down active camouflage system.")
    finally:
        stitcher.release()

if __name__ == "__main__":
    main()
