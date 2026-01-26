import cv2
import numpy as np


# Pause button (top-right)
pause_button_size = 50
pause_padding = 20

# Play button (center)
play_button_radius = 40

def draw_pause_button(frame):
    h, w = frame.shape[:2]
    x = w - pause_button_size - pause_padding
    y = pause_padding
    cv2.rectangle(frame, (x, y), (x + pause_button_size, y + pause_button_size), (200, 200, 200), -1)
    cv2.rectangle(frame, (x + 10, y + 10), (x + 20, y + 40), (50, 50, 50), -1)
    cv2.rectangle(frame, (x + 30, y + 10), (x + 40, y + 40), (50, 50, 50), -1)

def is_pause_clicked(fingers, frame_w):
    x = frame_w - pause_button_size - pause_padding
    y = pause_padding
    for fx, fy in fingers:
        if x <= fx <= x + pause_button_size and y <= fy <= y + pause_button_size:
            return True
    return False

def draw_play_button(frame):
    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2

    # Triangle pointing right
    pts = np.array([
        [cx - 30, cy - 50],
        [cx - 30, cy + 50],
        [cx + 50, cy]
    ], dtype=np.int32)

    pts = pts.reshape((-1, 1, 2))  # Make sure it's (n, 1, 2)

    cv2.fillPoly(frame, [pts], (50, 50, 50))  # ✅ No UMat
    cv2.polylines(frame, [pts], isClosed=True, color=(255, 255, 255), thickness=2)


def is_play_clicked(fingers, frame_w, frame_h):
    cx, cy = frame_w // 2, frame_h // 2
    for fx, fy in fingers:
        if (fx - cx) ** 2 + (fy - cy) ** 2 <= play_button_radius ** 2:
            return True
    return False
