import uuid

import cv2
import numpy as np
from loguru import logger

from processor.app import app
from processor.core.config import settings
from processor.images.agents_helper import AgentNames, AgentTopic
from processor.images.agents_transformer import AgentTransformers
from processor.images.models import ProcessorInput
from processor.images.opencv_helper import OpencvHelper
from processor.images.workflow import AgentConfig


# This agent derives input channel from settings file, as it is the interface to the world
@app.agent(channel=settings.PROCESSOR_INPUT_TOPIC)
async def agent_gateway(stream):
    async for event in stream:
        if isinstance(event, ProcessorInput):
            logger.bind().info(f"agent_gateway received data")
            event.id = uuid.uuid4()
            logger.bind(id=event.id).info(f"attached id")
            next_agent_config = await release_current_acquire_next(AgentNames.AGENT_GATEWAY, event)
            await send_data(next_agent_config, event)


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent1"))
async def agent1(stream):
    async for event in stream:
        logger.bind(id=event.id).info(f"agent1 received data")
        next_agent_config = await release_current_acquire_next(AgentNames.AGENT1, event)
        await send_data(next_agent_config, event)


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent_b"))
async def agent_b(stream):
    async for event in stream:
        logger.bind(id=event.id).info(f"agent_b received data")
        next_agent_config = await release_current_acquire_next(AgentNames.AGENT_B, event)
        await send_data(next_agent_config, event)


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent_transformer_color_bgr2gray"))
async def agent_transformer_color_bgr2gray(stream):
    async for event in stream:
        logger.bind(id=event.id).info(f"agent_transformer_color_bgr2gray received data")
        frame = OpencvHelper.list_to_ndarray(event.data) #np.array(event.data)
        logger.bind(id=event.id).info(f"frame deserialized ... ") ## type: {type(frame)}, shape:{frame.shape}
        new_frame = await AgentTransformers.transformer_color_BGR2GRAY(frame)
        logger.bind(id=event.id).info("new_frame received ...")
        event.data = OpencvHelper.ndarray_to_list(new_frame) #new_frame.tolist()
        next_agent_config = await release_current_acquire_next(AgentNames.AGENT_TRANSFORMER_COLOR_BGR2GRAY, event)
        await send_data(next_agent_config, event)


@app.agent(channel=AgentTopic.get_agent_input_channel_name("agent_save_to_disk"))
async def agent_save_to_disk(stream):
    async for event in stream:
        logger.bind(id=event.id).info(f"agent_save_to_disk received data")
        frame = np.array(event.data)
        cv2.imwrite('test1.png', frame)

        next_agent_config = await release_current_acquire_next(AgentNames.AGENT_SAVE_TO_DISK, event)
        await send_data(next_agent_config, event)


async def release_current_acquire_next(current_agent_name: str, event: ProcessorInput) -> AgentConfig:
    try:
        event.workflow.release_agent_config(current_agent_name)
        next_agent_config = event.workflow.acquire_next_agent_config()
        return next_agent_config
    except Exception as e:
        logger.bind(id=event.id).error(f"error: {e}")


async def send_data(next_agent_config: AgentConfig, event: ProcessorInput):
    if next_agent_config:
        # logger.bind().debug(f"next_agent: {next_agent_config.agent_name}")
        await app.send(channel=next_agent_config.agent_input_channel, value=event)
    else:
        logger.bind(id=event.id).info(f"next_agent: None")
