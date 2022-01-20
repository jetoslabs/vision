import faust
from faust import TopicT

from processor.core.config import settings
from processor.images.models import Image

app: faust.App = faust.App(
    settings.ID,
    version=1,
    autodiscover=True,
    origin='processor'
)

# processor_input_topic: TopicT = app.topic(settings.PROCESSOR_INPUT_TOPIC, value_type=Image)
channel1 = app.channel(value_type=Image)


if __name__ == '__main__':
    app.main()
