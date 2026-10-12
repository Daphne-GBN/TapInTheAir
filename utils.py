import math


def get_tile_color(level):
    if level <= 5:
        return (255, 255, 0)  # Yellow (Easy)
    elif level <= 12:
        return (255, 0, 255)  # Magenta (Medium)
    else:
        return (0, 255, 255)  # Cyan (Hard)


def is_finger_on_button(fingers, x, y, w, h):
    for fx, fy in fingers:
        if x < fx < x + w and y < fy < y + h:
            return True
    return False


def is_fingertip_on_tile(fingers, tile_x, tile_y, radius):
    """Return True when any fingertip is inside the circular tile."""
    radius_squared = radius * radius
    for fx, fy in fingers:
        dx = fx - tile_x
        dy = fy - tile_y
        if dx * dx + dy * dy <= radius_squared:
            return True
    return False
