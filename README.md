# 🎶 TapInTheAir ✋

**TapInTheAir** is a gesture-controlled rhythm game where players tap falling musical notes **in mid-air** using real-time hand tracking. No keyboard. No mouse. Just your hands and music.

Built using computer vision and audio processing, TapInTheAir turns natural finger movements into an interactive musical experience.

---

## 🚀 Features
- ✋ Real-time hand & fingertip tracking
- 🎵 Falling musical tiles with instant sound feedback
- 🧠 Gesture-based gameplay (no physical controllers)
- 📈 Dynamic difficulty scaling with levels
- ⏸ Pause & resume using gestures
- 🖥 Fullscreen support

---

## 🛠 Tech Stack
- **Python**
- **OpenCV** – video capture & rendering
- **MediaPipe** – hand tracking
- **Pygame** – audio playback
- **NumPy** – math & geometry

---

## 🎮 How It Works
1. Webcam captures live video frames
2. MediaPipe detects fingertip positions
3. Musical tiles fall from the top of the screen
4. Tap a tile in mid-air within the hit zone
5. A musical note plays and score updates instantly

---

## ▶️ How to Run
Make sure you have Python installed, then: 

 --bash
pip install opencv-python mediapipe pygame numpy
python main.py --
📷 Ensure your webcam is enabled before starting.
---

## 📂 Project Structure
graph TD
    A[TapInTheAir] --> B[main.py]
    A --> C[hand_tracker.py]
    A --> D[musical_tile.py]
    A --> E[hud.py]
    A --> F[pause.py]
    A --> G[game_states.py]
    A --> H[utils.py]
    A --> I[assets]
    I --> J[sounds]
    J --> K[note1.wav]
    J --> L[note2.wav]
    J --> M[note3.wav]
    J --> N[note4.wav]
    J --> O[note5.wav]
---
## 💡 Use Case

TapInTheAir demonstrates natural user interfaces, real-time computer vision, and interactive audio systems, making it ideal for:

Hackathons
Computer vision demos
Game programming portfolios
Gesture-based UI experiments
---

## 🧠 Future Enhancements

Beat-synced tile spawning
Combo & multiplier system
Visual hit effects
Gesture calibration
Multiplayer or song modes
---

## 👤 Author
Built with ❤️ by Daphne GBN

