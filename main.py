import cv2
import pygame
import random
import time
from pathlib import Path

from hand_tracker import HandTracker
from musical_tile import MusicalTile
import hud
import utils
import game_states
import pause


# Resolve assets relative to this file so the game works from any working directory.
ASSET_DIR = Path(__file__).resolve().parent / "Assets" / "sounds"

# Initialize pygame mixer and load sounds.
pygame.mixer.init()
window_name = "TapInTheAir"

sounds = [
    pygame.mixer.Sound(str(ASSET_DIR / "note1.wav")),
    pygame.mixer.Sound(str(ASSET_DIR / "note2.wav")),
    pygame.mixer.Sound(str(ASSET_DIR / "note3.wav")),
    pygame.mixer.Sound(str(ASSET_DIR / "note4.wav")),
    pygame.mixer.Sound(str(ASSET_DIR / "note5.wav")),
]

# Initialize tracker and camera.
tracker = HandTracker()
cap = cv2.VideoCapture(0)

# Fail clearly if the webcam cannot be opened instead of silently exiting.
if not cap.isOpened():
    cap.release()
    tracker.close()
    pygame.mixer.quit()
    raise RuntimeError(
        "Could not open the webcam. Check that it is connected and not being "
        "used by another application."
    )

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
PAUSED = 3
state = MENU

# Frame control variables
prev_frame_time = 0
new_frame_time = 0

# Hit line and trigger zone
hit_line_y = 300
trigger_zone = 30

# Scoring variables
score = 0
misses = 0
max_misses = 5
level = 1
level_threshold = 10  # Increase level every 10 points

# Tiles list
tiles = []

# Button dimensions (for menu)
button_w, button_h = 200, 100

# Fullscreen toggle variables
fullscreen = False
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

try:
    while True:
        success, frame = cap.read()
        if not success:
            print("Could not read a frame from the webcam. Exiting the game.")
            break

        frame = cv2.flip(frame, 1)
        frame_h, frame_w = frame.shape[:2]
        button_x = (frame_w - button_w) // 2
        button_y = (frame_h - button_h) // 2

        # Get finger positions
        frame, fingers = tracker.find_finger_positions(frame)

        # Frame rate calculation
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time + 0.00001)
        prev_frame_time = new_frame_time

        if state == MENU:
            if game_states.menu_state(frame, fingers, button_x, button_y, button_w, button_h):
                state = PLAYING
                score = 0
                misses = 0
                level = 1
                tiles = []

        elif state == PLAYING:
            # Update level based on score
            level = max(1, score // level_threshold + 1)

            # Draw hit line
            cv2.line(frame, (0, hit_line_y), (frame_w, hit_line_y), (255, 0, 0), 2)

            # Show pause button
            pause.draw_pause_button(frame)
            if pause.is_pause_clicked(fingers, frame_w):
                state = PAUSED
                time.sleep(0.5)

            # Spawn control based on level
            if level <= 5:
                spawn_chance = 45
                min_speed = 2
                max_speed = 4
            elif level <= 12:
                spawn_chance = 30
                min_speed = 4
                max_speed = 6
            else:
                spawn_chance = 20
                min_speed = 5
                max_speed = 8

            if random.randint(1, spawn_chance) == 1:
                note_index = random.randint(0, len(sounds) - 1)
                speed = random.randint(min_speed, max_speed)
                color = utils.get_tile_color(level)
                tiles.append(MusicalTile(note_index, speed, color, frame_w, sounds[note_index]))

            # Update and draw tiles
            for tile in tiles[:]:
                tile.update()
                tile.draw(frame)

                # Only score a tap when the tile is near the hit line and a
                # fingertip is inside the tile's circular boundary.
                within_hit_zone = abs(tile.y - hit_line_y) <= trigger_zone
                if (
                    not tile.played
                    and within_hit_zone
                    and utils.is_fingertip_on_tile(
                        fingers, tile.x, tile.y, tile.radius
                    )
                ):
                    tile.play()
                    score += 1

                # Miss detection and tile removal
                if tile.y > frame_h and not tile.played:
                    misses += 1
                    tiles.remove(tile)
                elif tile.played:
                    tiles.remove(tile)

            # Draw HUD
            hud.draw_score(frame, score)
            hud.draw_misses(frame, misses)
            hud.draw_level(frame, level)

            # Check for game over
            if misses >= max_misses:
                state = GAME_OVER
                over_time = time.time()

        elif state == PAUSED:
            pause.draw_play_button(frame)
            hud.draw_score(frame, score)
            hud.draw_misses(frame, misses)
            hud.draw_level(frame, level)

            # Resume check
            if pause.is_play_clicked(fingers, frame_w, frame_h):
                state = PLAYING
                time.sleep(0.5)

        elif state == GAME_OVER:
            if game_states.game_over_state(frame, score, over_time):
                state = MENU

        # Show the frame
        cv2.imshow(window_name, frame)

        # Key press handling
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key to quit
            break
        elif key == ord("f"):  # Toggle fullscreen
            fullscreen = not fullscreen
            if fullscreen:
                cv2.setWindowProperty(
                    window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
                )
            else:
                cv2.setWindowProperty(
                    window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL
                )
finally:
    # Release hardware and multimedia resources even if the loop exits with an error.
    cap.release()
    tracker.close()
    cv2.destroyAllWindows()
    pygame.mixer.quit()
