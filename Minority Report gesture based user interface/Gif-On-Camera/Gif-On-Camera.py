import cv2
import numpy as np
import imageio

# Load the GIF
gif_path = 'fireball-flame-ball.gif'
gif = imageio.mimread(gif_path)
frame_index = 0

# Open the webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Resize the GIF frame to match the camera frame size
    gif_frame = cv2.resize(gif[frame_index % len(gif)], (frame.shape[1], frame.shape[0]))

    # Overlay the GIF frame on top of the camera frame
    blended_frame = cv2.addWeighted(frame, 1, gif_frame, 0.5, 0)

    # Display the blended frame
    cv2.imshow('Camera with GIF', blended_frame)

    # Update the frame index to play the GIF
    frame_index += 1

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
