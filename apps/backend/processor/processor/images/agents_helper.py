import cv2 as cv


class Transformer:

    @staticmethod
    async def transformer_color_BGR2GRAY(frame):
        resulting_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return resulting_frame

    @staticmethod
    async def transformer_color_BGR2LAB(frame):
        resulting_frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
        return resulting_frame
