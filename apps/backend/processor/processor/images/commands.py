import uuid
from typing import Optional

import cv2 as cv
from loguru import logger
from numpy import ndarray

from processor.app import app
from processor.core.config import settings
from processor.images.commands_helper import video_capture
from processor.images.models import ProcessorInput
from processor.images.opencv_helper import OpencvHelper
from processor.images.workflow import WorkflowFactory


# @app.timer(10.0)
# async def populate():
#     processor_input = ProcessorInput(
#         workflow=WorkflowFactory.create_workflow(["agent1"]),
#         data=b'303'
#     )
#     # print(f"populate timer created data: {processor_input.dumps(serializer='json')}")
#     await app.send(channel=settings.PROCESSOR_INPUT_TOPIC, value=processor_input)


@app.timer(10.0)
async def capture_frame():
    frame: Optional[ndarray] = video_capture()
    resized_frame = cv.resize(frame, (320, 180))
    logger.bind().info(f"resized_frame .. type: {type(resized_frame)}, shape: {resized_frame.shape}")
    processor_input = ProcessorInput(
        # id=uuid.uuid4(),
        workflow=WorkflowFactory.create_workflow([
            # "agent1", "agent_b",
            "agent_transformer_color_bgr2gray", "agent_save_to_disk"
        ]),
        data= OpencvHelper.ndarray_to_list(resized_frame)
    )
    logger.bind().info(f"processor_input.data .. type: {type(processor_input.data)}")
    await app.send(channel=settings.PROCESSOR_INPUT_TOPIC, value=processor_input)
