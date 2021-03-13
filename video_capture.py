import cv2

class videoCapture():
    def __init__(self):
        cv2.namedWindow("webcam")
        self.vc = cv2.VideoCapture(0)

    def video(self):
        if self.vc.isOpened():
            rval, frame = self.vc.read()
        else:
            rval = False

        if rval:
            cv2.imshow("webcam", frame)
            rval, frame = self.vc.read()
            key = cv2.waitKey(20)
            if key == 27: #Escape key
                return "break"

            return frame.shape
