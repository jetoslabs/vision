import cv2
import numpy as np
from loguru import logger

from processor.app import app
from processor.core.config import settings
from processor.images.agents_helper import AgentNames, AgentTopic
from processor.images.models import ProcessorInput
from processor.images.workflow import AgentConfig

# This agent derives input channel from settings file, as it is the interface to the world
@app.agent(channel=settings.PROCESSOR_INPUT_TOPIC)
async def agent_gateway(stream):
    async for event in stream:
        if isinstance(event, ProcessorInput):
            logger.bind().info(f"agent_gateway received data")
            next_agent_config = await release_current_acquire_next(AgentNames.AGENT_GATEWAY, event)
            await send_data(next_agent_config, event)


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent1"))
async def agent1(stream):
    async for event in stream:
        logger.bind().info(f"agent1 received data")
        next_agent_config = await release_current_acquire_next(AgentNames.AGENT1, event)
        await send_data(next_agent_config, event)


# @app.agent(channel=processor_input_topic)
# async def agent0(stream):
#     event: MyModel
#     async for event in stream:
#         print(f"agent0 received: {str(event)}")
#         # yield event
#         await app.send(channel=get_agent_input_channel_name("agent1"), value=event)


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent_b"))
async def agent_b(stream):
    async for event in stream:
        logger.bind().info(f"agent_b received data")
        next_agent_config = await release_current_acquire_next(AgentNames.AGENT_B, event)
        await send_data(next_agent_config, event)


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


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent_save_to_disk"))
async def agent_save_to_disk(stream):
    async for event in stream:
        logger.bind().info(f"agent_save_to_disk received data")
        frame = np.array(event.data)
        cv2.imwrite('test1.png', frame)

        next_agent_config = await release_current_acquire_next(AgentNames.AGENT_SAVE_TO_DISK, event)
        await send_data(next_agent_config, event)


# async def release_and_send(event: ProcessorInput, agent_name: str):
#     try:
#         event.workflow.release_agent_config(agent_name)
#         next_agent_config = event.workflow.acquire_next_agent_config()
#         if next_agent_config:
#             await app.send(channel=next_agent_config.agent_input_channel, value=event)
#     except Exception as e:
#         logger.bind().error(f"error: {e}")


async def release_current_acquire_next(current_agent_name: str, event: ProcessorInput) -> AgentConfig:
    try:
        event.workflow.release_agent_config(current_agent_name)
        next_agent_config = event.workflow.acquire_next_agent_config()
        return next_agent_config
    except Exception as e:
        logger.bind().error(f"error: {e}")


async def send_data(next_agent_config: AgentConfig, event: ProcessorInput):
    if next_agent_config:
        # logger.bind().debug(f"next_agent: {next_agent_config.agent_name}")
        await app.send(channel=next_agent_config.agent_input_channel, value=event)
    else:
        logger.bind().info(f"next_agent: None")
