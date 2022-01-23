from typing import Optional


def get_agent_input_channel_name(agent_name: str) -> Optional[str]:
    if agent_name == "":
        return None
    return _eval_agent_input_channel_name(agent_name)


def _eval_agent_input_channel_name(agent_name: str) -> str:
    input_channel_name = f"{agent_name.lower()}-input-topic"
    return input_channel_name