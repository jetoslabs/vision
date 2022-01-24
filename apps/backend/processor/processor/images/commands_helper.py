from time import sleep
from typing import Any, Optional

import cv2 as cv
from loguru import logger
from numpy import ndarray


def video_capture(src: int = 0) -> Optional[ndarray]:
    cap: cv.VideoCapture = cv.VideoCapture(src)
    try:
        sleep(0.1)  # to get clear frame
        ret, frame = cap.read()
        if ret is True:
            return frame

        logger.bind().debug("capture_frame was not successful")
        return None
    except Exception as e:
        logger.bind().error(f"Error in capture_frame:\n {e}")
    finally:
        if cap is not None:
            cap.release()


