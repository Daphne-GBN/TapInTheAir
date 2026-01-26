import cv2

def draw_score(frame, score):
    cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def draw_misses(frame, misses):
    cv2.putText(frame, f"Misses: {misses}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def draw_level(frame, level):
    cv2.putText(frame, f"Level: {level}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
