import cv2 as cv
from numpy import ndarray


class AgentTransformers:

    @staticmethod
    async def transformer_color_BGR2GRAY(frame: ndarray) -> ndarray:
        resulting_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return resulting_frame

    @staticmethod
    async def transformer_color_BGR2LAB(frame: ndarray) -> ndarray:
        resulting_frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
        return resulting_frame
