import cv2 as cv
import numpy
import numpy as np


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


# def get_one_frame():
#     cap = cv.VideoCapture(0)
#     try:
#         ret, frame = cap.read()
#         cv.imwrite("original.png", frame)
#         ######  serialize
#         # flatten multi-dim array (but still a ndarray type)
#         ret, buffer = cv.imencode('.png', frame)
#         # still dont know why we require this step. But without this step frame after deserializing is not the same
#         buffer_to_array = np.array(buffer)
#         data_encode = buffer_to_array.tobytes()
#         ######  deserialize
#         image_array = np.asarray(bytearray(data_encode), dtype='uint8')
#         frame_de = cv.imdecode(image_array, cv.IMREAD_COLOR)
#         ######
#         result = cv.cvtColor(frame_de, cv.COLOR_BGR2GRAY)
#         cv.imwrite("result.png", result)
#     except Exception as e:
#         print(e)


def serialize_for_faust(frame: numpy.ndarray):
    # flatten multi-dim array (but still a ndarray type)
    ret, buffer = cv.imencode('.png', frame)
    # still dont know why we require this step. But without this step frame after deserializing is not the same
    # buffer_to_array = np.array(buffer)
    # data_encode = buffer_to_array.tobytes()
    frame_ser = buffer.tobytes()
    return frame_ser


def deserialize_for_faust(data_encode):
    image_array = np.asarray(bytearray(data_encode), dtype='uint8')
    frame_de = cv.imdecode(image_array, cv.IMREAD_COLOR)
    return frame_de
