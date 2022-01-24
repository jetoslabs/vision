

# Agent names (is equal to method name of the agent)
from typing import Optional


class AgentNames:
    AGENT_GATEWAY = "agent_gateway"
    AGENT1 = "agent1"
    AGENT_B = "agent_b"
    AGENT_C = "agent_c"
    AGENT_SAVE_TO_DISK = "agent_save_to_disk"


class AgentTopic:
    @staticmethod
    def get_agent_input_channel_name(agent_name: str) -> Optional[str]:
        if agent_name == "":
            return None
        return AgentTopic._eval_agent_input_channel_name(agent_name)

    @staticmethod
    def _eval_agent_input_channel_name(agent_name: str) -> str:
        input_channel_name = f"{agent_name.lower()}-input-topic"
        return input_channel_name
