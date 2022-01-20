from typing import Optional

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


def get_agent_input_channel_name(agent_name: str) -> Optional[str]:
    if agent_name == "":
        return None
    return _eval_agent_input_channel_name(agent_name)


def _eval_agent_input_channel_name(agent_name: str) -> str:
    input_channel_name = f"{agent_name.lower()}-input-ch"
    return input_channel_name