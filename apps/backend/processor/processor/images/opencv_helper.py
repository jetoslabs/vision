import cv2 as cv
import numpy as np


def serialize_for_faust(frame: np.ndarray):
    # flatten multi-dim array (but still a ndarray type)
    ret, buffer = cv.imencode('.png', frame)
    # encode to bytes
    frame_ser = buffer.tobytes()
    return frame_ser


def deserialize_for_faust(data_encode):
    # get flat ndarray from frame serialized to bytes
    image_array = np.asarray(bytearray(data_encode), dtype='uint8')
    # get multi-dim ndarray (original opencv frame format)
    frame_de = cv.imdecode(image_array, cv.IMREAD_COLOR)
    return frame_de
