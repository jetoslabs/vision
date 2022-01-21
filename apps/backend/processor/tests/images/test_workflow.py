from processor.core.config import settings
from processor.images.workflow import WorkflowFactory


def test_create_workflow():
    agent_names = ["agent_a", "agent1"]

    workflow = WorkflowFactory.create_workflow(agent_names)

    assert len(workflow.flows) - 1 == len(agent_names)
    assert workflow.flows[0].agent_input_channel == settings.PROCESSOR_INPUT_TOPIC


def test_create_workflow_empty_list():
    agent_names = []

    workflow = WorkflowFactory.create_workflow(agent_names)

    assert len(workflow.flows) - 1 == len(agent_names)
    assert workflow.flows[0].agent_input_channel == settings.PROCESSOR_INPUT_TOPIC