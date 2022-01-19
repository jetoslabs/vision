from typing import Any, Optional

import cv2 as cv
from loguru import logger


def video_capture(src: int = 0) -> Optional[Any]:
    cap: cv.VideoCapture = cv.VideoCapture(src)
    try:
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


