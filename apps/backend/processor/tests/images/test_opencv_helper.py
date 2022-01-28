from time import sleep

import cv2 as cv

from processor.images.opencv_helper import OpencvHelper


def test_opencv_serde():
    assert opencv_serde()


def opencv_serde():
    cap = cv.VideoCapture(0)
    sleep(0.1)
    try:
        ret, frame = cap.read()
        cv.imwrite("original.png", frame)
        #  serialize
        frame_ser = OpencvHelper.ndarray_to_list(frame)
        #  deserialize
        frame_de = OpencvHelper.list_to_ndarray(frame_ser)
        ######
        result = cv.cvtColor(frame_de, cv.COLOR_BGR2GRAY)
        cv.imwrite("result.png", result)
        return True
    except Exception as e:
        print(e)
        return False
