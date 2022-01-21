from loguru import logger

from processor.app import app
from processor.core.config import settings
from processor.images.agents_helper import get_agent_input_channel_name
from processor.images.agents_helper import Transformer
from processor.images.models import MyModel, Timing


# This agent derives input channel from settings file, as it is the interface to the world
@app.agent(channel=settings.PROCESSOR_INPUT_TOPIC)
async def agent_gateway(stream):
    async for event in stream:
        try:
            print(f"agent_gateway received: {str(event)}")
            # TODO: write code to send to next agent in workflow, OR read docs for class layout of Agent (to send msg)
        except Exception as e:
            logger.bind().error(f"error: {e}")


@app.agent(channel=get_agent_input_channel_name("agent1"))
async def agent1(stream):
    async for event in stream:
        print(f"agent1 received: {str(event)}")


# @app.agent(channel=processor_input_topic)
# async def agent0(stream):
#     event: MyModel
#     async for event in stream:
#         print(f"agent0 received: {str(event)}")
#         # yield event
#         await app.send(channel=get_agent_input_channel_name("agent1"), value=event)


@app.agent(channel=get_agent_input_channel_name("agent_b"))
async def agent_b(stream):
    async for event in stream:
        print(f'AGENT B RECEIVED: {event!r}')


# @app.agent(channel=processor_input_topic)
# async def agent_a(stream):
#     async for event in stream:
#         timing: Timing
#         print(f'AGENT A RECEIVED: {event!r}')
#         # yield event
#         await app.send(channel=get_agent_input_channel_name("agent_b"), value=event)


# @app.agent(channel=processor_input_topic)
# async def agent_transformer_color_BGR2GRAY(stream):
#     async for event in stream:
#         frame = await Transformer.transformer_color_BGR2GRAY(event.data)
#         print(f'AGENT A RECEIVED: {frame!r}')
#         yield frame
