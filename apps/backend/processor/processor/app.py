import faust
from faust import TopicT

from processor.images.models import Image

app: faust.App = faust.App(
    'vision_processor',
    version=1,
    autodiscover=True,
    origin='processor'
)

topic: TopicT = app.topic('processor_input', value_type=Image)
channel1 = app.channel(value_type=Image)


if __name__ == '__main__':
    app.main()
