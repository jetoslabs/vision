import cv2 as cv


class Transformer:

    @staticmethod
    async def transformer_color_BGR2GRAY(frame):
        resulting_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return resulting_frame

    @staticmethod
    async def transformer_color_BGR2LAB(frame):
        resulting_frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
        return resulting_frame

# def release_current_and_send_to_next_in_workflow(workflow: Workflow, msg: Any) -> bool:
#     next_agent_config = workflow.acquire_next_agent_config()
#     workflow.release_agent_config()
