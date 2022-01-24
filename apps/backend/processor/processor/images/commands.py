import json
from datetime import datetime
import cv2 as cv
from processor.app import app
from processor.core.config import settings
from processor.core.logs import generate_trace_id
from processor.images.commands_helper import video_capture
from processor.images.models import ProcessorInput
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
    frame = video_capture()
    resized_frame = cv.resize(frame, (176, 144))
    processor_input = ProcessorInput(
        workflow=WorkflowFactory.create_workflow(["agent1", "agent_b", "agent_save_to_disk"]),
        data=resized_frame.tolist()
    )
    await app.send(channel=settings.PROCESSOR_INPUT_TOPIC, value=processor_input)
