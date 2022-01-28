import cv2 as cv
import numpy
import numpy as np
import base64
from loguru import logger


class OpencvHelper:
    @staticmethod
    def ndarray_to_list(frame: np.ndarray) -> list:
        im_list: list = frame.tolist()
        return im_list

    @staticmethod
    def list_to_ndarray(im_list) -> np.ndarray:
        frame = numpy.array(im_list, dtype='uint8')
        return frame


# def opencv_to_bytes(frame: np.ndarray):
#     # flatten multi-dim array (but still a ndarray type)
#     ret, buffer = cv.imencode('.png', frame)
#     # encode to bytes
#     frame_ser = buffer.tobytes()
#     return frame_ser


# def bytes_to_opencv(data_encode):
#     # get flat ndarray from frame serialized to bytes
#     image_array = np.asarray(bytearray(data_encode), dtype='uint8')
#     # get multi-dim ndarray (original opencv frame format)
#     frame_de = cv.imdecode(image_array, cv.IMREAD_COLOR)
#     return frame_de


# def opencv_to_base64(frame: np.ndarray) -> str:
#     ret, im_arr = cv.imencode('.png', frame)
#     im_b64 = im_arr.tostring()
#     print(f"type of im_64: {type(im_b64)}")
#     # im_bytes = im_arr.tobytes()
#     # im_b64 = base64.b64encode(im_bytes)
#     # write_to_file("cv_to_b64", im_b64)
#     logger.bind().info(f"type of im_b64: {type(im_b64)}")
#     return im_b64


# # def base64_to_opencv(im_b64: bytes) -> np.ndarray:
# def base64_to_opencv(im_b64: str) -> np.ndarray:
#     logger.bind().info(f"type of im_b64: {type(im_b64)}")
#     # write_to_file("b64_to_cv", im_b64)
#     # im_bytes = base64.b64decode(im_b64)
#     # im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
#     im_arr = np.fromstring(im_b64, np.uint8)
#     frame = cv.imdecode(im_arr, flags=cv.IMREAD_COLOR)
#     return frame
#

def write_to_file(file: str, data: bytes):
    with open(file, "wb") as binary_file:
        binary_file.write(data)
