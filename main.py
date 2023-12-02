import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
i_y = 0;

while True:
    _, frame =  cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    # print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmark = hand.landmark
            for i, landmark in enumerate(landmark):
                x = int(landmark.x * frame_width)
                y= int(landmark.y * frame_height)
                # print(x, y)
                if i == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    i_x = screen_width / frame_width * x
                    i_y = screen_height / frame_height * y
                    pyautogui.moveTo(i_x,i_y)
                if i == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 144))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    pyautogui.moveTo(thumb_x,thumb_y)
                    print('outside', abs(i_y-thumb_y))
                    if abs(i_y - thumb_y) < 20:
                        # print('clicked')
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)