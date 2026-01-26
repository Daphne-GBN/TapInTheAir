import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("assets/sounds/note1.wav")
sound.play()

# Wait long enough to hear it
import time
time.sleep(2)
