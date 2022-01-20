import datetime
from typing import Optional, List

import faust

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
    def __abstract_init__(self) -> None:
        pass

    workflow: Optional[Workflow]
    data: Optional[bytes]


# class Workflow(faust.Record):
#     def __abstract_init__(self) -> None:
#         pass
#
#     transformers: List[Transformer]
