import cv2 as cv
from processor.images.opencv_helper import serialize_for_faust, deserialize_for_faust


def test_opencv_serde():
    assert opencv_serde()


def opencv_serde():
    cap = cv.VideoCapture(0)
    try:
        ret, frame = cap.read()
        cv.imwrite("original.png", frame)
        #  serialize
        frame_ser = serialize_for_faust(frame)
        #  deserialize
        frame_de = deserialize_for_faust(frame_ser)
        ######
        result = cv.cvtColor(frame_de, cv.COLOR_BGR2GRAY)
        cv.imwrite("result.png", result)
        return True
    except Exception as e:
        print(e)
        return False
