import cv2
import numpy as np
from loguru import logger

from processor.app import app
from processor.core.config import settings

from processor.images.agents_topic import get_agent_input_channel_name

from processor.images.models import ProcessorInput

# Agent names (is equal to method name of the agent)
AGENT_GATEWAY = "agent_gateway"
AGENT1 = "agent1"
AGENT_B = "agent_b"
AGENT_C = "agent_c"
AGENT_SAVE_TO_DISK = "agent_save_to_disk"


# This agent derives input channel from settings file, as it is the interface to the world
@app.agent(channel=settings.PROCESSOR_INPUT_TOPIC)
async def agent_gateway(stream):
    async for event in stream:
        if isinstance(event, ProcessorInput):
            # # logger.bind().error(type(event.data))
            # try:
            #     # TODO: write code to send to next agent in workflow, OR read docs for class layout of Agent (to send msg)
            #     marked_is_done = event.workflow.release_agent_config(AGENT_GATEWAY)
            #
            #     next_agent_config = event.workflow.acquire_next_agent_config()
            #     logger.bind().info(f"agent_gateway processed data with workflow: {str(event.workflow)}")
            #     if next_agent_config:
            #         await app.send(channel=next_agent_config.agent_input_channel, value=event)
            # except Exception as e:
            #     logger.bind().error(f"error: {e}")
            logger.bind().info(f"agent_gateway received data with workflow: {str(event.workflow)}")
            await release_and_send(event, AGENT_GATEWAY)


@app.agent(channel=get_agent_input_channel_name("agent1"))
async def agent1(stream):
    async for event in stream:
        # try:
        #     event.workflow.release_agent_config(AGENT1)
        #     next_agent_config = event.workflow.acquire_next_agent_config()
        #     logger.bind().info(f"agent1 processed data with workflow: {str(event.workflow)}")
        #     if next_agent_config:
        #         await app.send(channel=next_agent_config.agent_input_channel, value=event)
        # except Exception as e:
        #     logger.bind().error(f"error: {e}")
        logger.bind().info(f"agent1 received data with workflow: {str(event.workflow)}")
        await release_and_send(event, AGENT1)


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
        # try:
        #     event.workflow.release_agent_config(AGENT_B)
        #     next_agent_config = event.workflow.acquire_next_agent_config()
        #     logger.bind().info(f"agent_b processed data with workflow: {str(event.workflow)}")
        #     if next_agent_config:
        #         await app.send(channel=next_agent_config.agent_input_channel, value=event)
        # except Exception as e:
        #     logger.bind().error(f"error: {e}")
        logger.bind().info(f"agent_b received data with workflow: {str(event.workflow)}")
        await release_and_send(event, AGENT_B)


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

#
@app.agent(channel=get_agent_input_channel_name("agent_save_to_disk"))
async def agent_save_to_disk(stream):
    async for event in stream:
        logger.bind().info(f"agent_save_to_disk received data with workflow: {str(event.workflow)}")
        frame = np.array(event.data)
        cv2.imwrite('test1.png', frame)


async def release_and_send(event: ProcessorInput, agent_name: str):
    try:
        event.workflow.release_agent_config(agent_name)
        next_agent_config = event.workflow.acquire_next_agent_config()
        if next_agent_config:
            await app.send(channel=next_agent_config.agent_input_channel, value=event)
    except Exception as e:
        logger.bind().error(f"error: {e}")
