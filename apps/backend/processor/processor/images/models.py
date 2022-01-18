import datetime
from typing import Optional, List

import faust

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


class Image(faust.Record):
    def __abstract_init__(self) -> None:
        pass

    trace_id: str
    timings: List[Timing]
    data: Optional[bytes]


# class Workflow(faust.Record):
#     def __abstract_init__(self) -> None:
#         pass
#
#     transformers: List[Transformer]
