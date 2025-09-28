# 🖐️ Hand Mouse – Mouse control with hand gestures

This project allows you to control your computer mouse using your **webcam** and **hand gestures** detected with [MediaPipe](https://developers.google.com/mediapipe) and [OpenCV](https://opencv.org/).
After a brief calibration process, you'll be able to move the cursor and click with your hand.

## 🚀 Main Features

- Move the cursor based on the position of your index finger.
- Click by closing your thumb.
- Detect special gestures such as the fingertip gesture (closes the program).
- Automatic calibration of the open and closed hand to adapt to each user.

## 📦 Requirements
pip install opencv-python mediapipe pyautogui numpy

## ▶️ Usage
1. Connect a webcam and run the main program:

    python main.py

2. Calibration takes place during the first few seconds:
    - Place your hand in the indicated position.
    - Close your hand when prompted.
    - Open it when prompted.

3. Once calibrated:
    - Move your index finger to control the cursor.
    - Close your thumb to click.
    - Give the finger to close the program.
    - You can also exit by pressing the q key.

## 📂 Project Structure
```
.
├── main.py             # Main program: manages camera, calibration, and control
├── calibracion.py      # Logic to calculate open/closed finger thresholds
├── detectar_gestos.py  # Functions to detect open/closed fingers and gestures
├── mover_raton.py      # Cursor and click control using pyautogui
├── posiciones.py       # Obtaining coordinates (TIP and MCP) for each finger
```
## ⚙️ Flow Explanation
1. main.py opens the camera and draws the hand on the screen.
2. Calibration is performed to calculate the thresholds between open and closed hands.
3. Once calibrated:
    - Call mover_raton.moveRaton() to move the cursor.
    - Gestures are detected with detect_gestures.
    - If the thumb moves from open to closed, a click is executed (mover_raton.clickRaton()).
    - If the comb is detected, the program closes.

## 🔮 Possible improvements
- Add double-click or right-click with new gestures.
- Dynamically adjust cursor sensitivity.
- Support for multiple hands.
- Configure custom gestures.

## 👨‍💻 Author
Project developed by Alejandro Lara Lara, using Python, OpenCV, and MediaPipe.