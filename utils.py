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
