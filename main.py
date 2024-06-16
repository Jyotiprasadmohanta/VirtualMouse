import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
drawing_utils = mp.solutions.drawing_utils
hand_detector = mp.solutions.hands.Hands()
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x*frame_width)
                y = int(landmarks.y*frame_width)
                print(x,y)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)