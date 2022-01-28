import datetime
from typing import Optional, List

import faust
from uuid import UUID

from processor.images.workflow import Workflow


class MyModel(faust.Record):
    def __abstract_init__(self) -> None:
        pass
    x: int


class MyModel1(faust.Record):
    def __abstract_init__(self) -> None:
        pass
    y: int


class Timing(faust.Record):
    def __abstract_init__(self) -> None:
        pass
    name: str
    start_time: Optional[datetime.datetime]
    end_time: Optional[datetime.datetime]
    time_taken_msec: Optional[float]


class ProcessorInput(faust.Record):
    """
    Input to processor (agent_gateway)
    Params:
        id: Optional[UUID]
        workflow: Optional[Workflow]
        data: Optional[bytes]
    """
    def __abstract_init__(self) -> None:
        pass

    id: Optional[UUID]
    workflow: Optional[Workflow]
    data: Optional[list]


# class Workflow(faust.Record):
#     def __abstract_init__(self) -> None:
#         pass
#
#     transformers: List[Transformer]
