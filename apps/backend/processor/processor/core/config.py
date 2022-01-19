from pydantic import BaseSettings


class Config(BaseSettings):
    NAME: str = "Vision Processor"
    ID: str = "vision-processor"
    APP_DEBUG = True

    # Topics
    PROCESSOR_INPUT_TOPIC = "processor_input_topic"
    WORKFLOW_OUTPUT_TOPIC_PREFIX = "workflow_output_topic_prefix"


settings = Config()
