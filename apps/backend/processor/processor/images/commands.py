from datetime import datetime

from processor.app import app, processor_input_topic
from processor.core.logs import generate_trace_id
from processor.images.commands_helper import video_capture
from processor.images.models import Image, Timing


@app.timer(1.0)
async def populate():
    image = Image(
        trace_id=await generate_trace_id(),
        timings=[Timing(
            name=populate.__name__,
            start_time=datetime.now()
        )],
        data=b'303'
    )
    await processor_input_topic.send(value=image)

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
#     await processor_input_topic.send(value=image)