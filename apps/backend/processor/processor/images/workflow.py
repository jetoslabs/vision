from typing import List, Any

import faust

from processor.core.config import settings
from processor.images.agents_helper import get_agent_input_channel_name


class AgentConfig(faust.Record):
    """
    AgentConfig holds details to reach a agent method \n
    Params:
        agent_name: str \n
        agent_input_channel: str \n
        is_done: bool
    """

    def __abstract_init__(self) -> None:
        pass

    agent_name: str
    agent_input_channel: str
    is_done: bool


class Workflow(faust.Record):
    """Workflow is ordered list of Agents that will process the data"""

    def __abstract_init__(self) -> None:
        pass

    flows: List[AgentConfig]

    def acquire_next_agent_config(self) -> AgentConfig:
        """For send, Agent acquires the next AgentConfig """
        for flow in self.flows:
            if not flow.is_done:
                return flow

    def release_agent_config(self, pos_in_flow: int = 1) -> bool:
        """Agent use this method mark that work is complete"""
        if pos_in_flow < 1 or pos_in_flow > len(self.flows):
            return False
        index_in_flow = pos_in_flow - 1
        for i in range(len(self.flows)):
            flow = self.flows[i]
            if not flow.is_done:
                if i == index_in_flow:
                    break
        self.flows[index_in_flow].is_done = True


class WorkflowFactory:
    @staticmethod
    def create_workflow(agent_names: List[str] = []) -> Workflow:
        """Factory method to create a Workflow"""
        # Every data's journey begins with agent_gateway
        agent_configs: List[AgentConfig] = [WorkflowFactory.create_agent_gateway_config()]

        for agent_name in agent_names:
            agent_config = WorkflowFactory.create_agent_config(agent_name)
            agent_configs.append(agent_config)

        workflow = Workflow(flows=agent_configs)
        return workflow

    @staticmethod
    def create_agent_config(agent_name: str) -> AgentConfig:
        """Factory method to create an AgentConfig"""
        agent_config = AgentConfig(
            agent_name=agent_name,
            agent_input_channel=get_agent_input_channel_name(agent_name),
            is_done=False
        )
        return agent_config

    @staticmethod
    def create_agent_gateway_config() -> AgentConfig:
        """Factory method to create an AgentGateway Config"""
        agent_config = AgentConfig(
            agent_name="agent_gateway",
            agent_input_channel=settings.PROCESSOR_INPUT_TOPIC,
            is_done=False
        )
        return agent_config
