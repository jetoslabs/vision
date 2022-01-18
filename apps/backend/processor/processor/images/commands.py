from datetime import datetime

from processor.app import app, topic
from processor.core.logs import generate_trace_id
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
    await topic.send(value=image)