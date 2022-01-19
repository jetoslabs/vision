from processor.app import app, channel1, processor_input_topic
from processor.images.agents_helper import Transformer
from processor.images.models import MyModel, Timing


@app.agent(channel=channel1)
async def agent1(stream):
    async for event in stream:
        print(f"agent1 received: {str(event)}")


@app.agent(channel=processor_input_topic, sink=[channel1])
async def agent0(stream):
    event: MyModel
    async for event in stream:
        print(f"agent0 received: {str(event)}")
        yield event
        # await app.send(channel=channel1, value=MyModel1(event.x))


@app.agent()
async def agent_b(stream):
    async for event in stream:
        print(f'AGENT B RECEIVED: {event!r}')


@app.agent(channel=processor_input_topic, sink=[agent_b])
async def agent_a(stream):
    async for event in stream:
        timing: Timing
        print(f'AGENT A RECEIVED: {event!r}')
        yield event


# @app.agent(channel=processor_input_topic)
# async def agent_transformer_color_BGR2GRAY(stream):
#     async for event in stream:
#         frame = await Transformer.transformer_color_BGR2GRAY(event.data)
#         print(f'AGENT A RECEIVED: {frame!r}')
#         yield frame
