"""
perspective_warp.py
Calculates and applies real-time perspective warping to match background views.
"""

import cv2
import numpy as np

class PerspectiveWarper:
    def __init__(self, src_pts, dst_pts):
        self.src_pts = np.float32(src_pts)
        self.dst_pts = np.float32(dst_pts)
        self.matrix = cv2.getPerspectiveTransform(self.src_pts, self.dst_pts)

    def apply_warp(self, frame, target_size=(1920, 1080)):
        warped = cv2.warpPerspective(frame, self.matrix, target_size)
        return warped

    def update_homography(self, new_src, new_dst):
        self.matrix = cv2.getPerspectiveTransform(np.float32(new_src), np.float32(new_dst))
