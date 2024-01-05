import cv2
import mediapipe as mp
import webbrowser

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands

# Initialize hand tracking
hands = mphands.Hands()

# Function to count fingers based on hand landmarks
def count_fingers(hand_landmarks):
    # Define landmarks for thumb and fingers
    thumb_tip = hand_landmarks.landmark[mphands.HandLandmark.THUMB_TIP].y
    index_tip = hand_landmarks.landmark[mphands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = hand_landmarks.landmark[mphands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = hand_landmarks.landmark[mphands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = hand_landmarks.landmark[mphands.HandLandmark.PINKY_TIP].y

    # Set a threshold for finger detection
    finger_open_threshold = 0.8

    # Check each finger for open/closed status
    fingers_open = [thumb_tip < index_tip,
                    index_tip < middle_tip,
                    middle_tip < ring_tip,
                    ring_tip < pinky_tip]

    # Count the number of open fingers
    count = sum(fingers_open)
    return count

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # Process the image and get hand landmarks
    result = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks and connections
            mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)

            # Count fingers and display the count
            finger_count = count_fingers(hand_landmarks)
            cv2.putText(image, f"Fingers: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Open Google if two fingers are detected
            if finger_count == 2:
                print("Hey")

    # Display the image
    cv2.imshow("Handtracker", image)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()
