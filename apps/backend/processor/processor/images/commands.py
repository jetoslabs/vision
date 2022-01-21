from datetime import datetime

from processor.app import app
from processor.core.config import settings
from processor.core.logs import generate_trace_id
from processor.images.commands_helper import video_capture
from processor.images.models import Timing, ProcessorInput
from processor.images.workflow import WorkflowFactory


@app.timer(1.0)
async def populate():
    processor_input = ProcessorInput(
        workflow=WorkflowFactory.create_workflow(["agent1"]),
        data=b'303'
    )
    await app.send(channel=settings.PROCESSOR_INPUT_TOPIC, value=processor_input)

# @app.timer(5.0)
# async def capture_frame():
#     image = Image(
#         trace_id=await generate_trace_id(),
#         timings=[Timing(
#             name=capture_frame.__name__,
#             start_time=datetime.now()
#         )],
#         data=video_capture()
#     )
#     await app.send(channel=settings.PROCESSOR_INPUT_TOPIC, value=image)
