import faust


class MyModel(faust.Record):
    def __abstract_init__(self) -> None:
        pass

    x: int

    def __str__(self):
        return f"x = {self.x}"


class MyModel1(faust.Record):
    def __abstract_init__(self) -> None:
        pass

    y: int

    def __str__(self):
        return f"y = {self.y}"
