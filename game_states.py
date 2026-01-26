import cv2
import time
from utils import is_finger_on_button

def draw_centered_text(frame, text, center_x, y, scale=0.7, color=(255, 255, 255), thickness=2):
    (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, scale, thickness)
    x = center_x - w // 2
    cv2.putText(frame, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)


def menu_state(frame, fingers, button_x, button_y, button_w, button_h):
    frame_h, frame_w = frame.shape[:2]
    center_x = frame_w // 2

    # Title
    draw_centered_text(frame, "TapInTheAir",
                       center_x, button_y - 110,
                       scale=1.2, color=(255, 0, 255), thickness=3)

    # Instructions
    draw_centered_text(frame, "Tap falling notes in the air",
                       center_x, button_y - 70)

    draw_centered_text(frame, "Use your fingers — no keyboard!",
                       center_x, button_y - 40)

    draw_centered_text(frame, "Tap ESC to quit!",
                       center_x, button_y - 10)

    # PLAY button
    cv2.rectangle(frame,
                  (button_x, button_y),
                  (button_x + button_w, button_y + button_h),
                  (0, 255, 0), -1)

    draw_centered_text(frame, "PLAY",
                       button_x + button_w // 2,
                       button_y + 65,
                       scale=1.0, color=(255, 255, 255), thickness=3)

    # Start game
    if fingers and is_finger_on_button(fingers, button_x, button_y, button_w, button_h):
        time.sleep(0.5)
        return True

    return False

    # Play button
    cv2.rectangle(
        frame,
        (button_x, button_y),
        (button_x + button_w, button_y + button_h),
        (0, 255, 0),
        -1
    )

    cv2.putText(frame, "PLAY",
                (button_x + 50, button_y + 65),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 3)

    # Check for play tap
    if fingers and is_finger_on_button(fingers, button_x, button_y, button_w, button_h):
        time.sleep(0.5)
        return True  # Start game

    return False


def game_over_state(frame, score, over_time):
    cv2.putText(frame, "GAME OVER",
                (150, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 2,
                (0, 0, 255), 4)

    cv2.putText(frame, f"Final Score: {score}",
                (150, 300),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                (255, 255, 255), 3)

    if time.time() - over_time > 3:
        return True  # Return to menu

    return False
