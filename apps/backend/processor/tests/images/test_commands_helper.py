from processor.images.commands_helper import video_capture
import cv2 as cv


def test_video_capture():
    frame = video_capture(0)
    # cv.imshow('frame', frame)
    # cv.waitKey(10)
    # cv.destroyAllWindows()
    assert frame is not None
