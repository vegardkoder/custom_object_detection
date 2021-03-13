from video_capture import videoCapture

vc  = videoCapture()

while True:
    video = vc.video()
    if video == "break":
        break

    print(video)
