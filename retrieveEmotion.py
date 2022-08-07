import cv2
from deepface import DeepFace
from edit import editPhoto


def retrieveEmotion(photo):

    face_cascade = cv2.CascadeClassifier(
        '/Users/michellechen/PycharmProjects/emotionEditor/haar_cascade.xml')
    cap = cv2.VideoCapture(0)

    while (True):
        ret, frame = cap.read()
        result = DeepFace.analyze(img_path=frame, actions=[
                                  'emotion'], enforce_detection=False)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            color = (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        emotion = result["dominant_emotion"]
        editPhoto(emotion, photo)
        cv2.putText(frame, str(emotion),
                    (50, 50, cv2.FONT_HERSHEY_PLAIN), 1, (0, 0, 255), 3)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
