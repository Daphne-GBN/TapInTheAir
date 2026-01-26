import cv2
import random

class MusicalTile:
    def __init__(self, note_index, speed, color, screen_width, sound):
        self.note_index = note_index
        self.speed = speed
        self.color = color
        self.x = random.randint(50, screen_width - 50)
        self.y = 0
        self.radius = 30
        self.played = False
        self.sound = sound

    def update(self):
        self.y += self.speed

    def draw(self, frame):
        # Convert RGB color to BGR for OpenCV
        bgr_color = (self.color[2], self.color[1], self.color[0])
        cv2.circle(frame, (self.x, self.y), self.radius, bgr_color, -1)

    def play(self):
        if not self.played:
            self.sound.play()
            self.played = True



