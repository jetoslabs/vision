import faust

from processor.core.config import settings
from processor.images.models import ProcessorInput

app: faust.App = faust.App(
    settings.ID,
    version=1,
    autodiscover=True,
    origin='processor'
)

# processor_input_topic: TopicT = app.topic(settings.PROCESSOR_INPUT_TOPIC, value_type=Image)
channel1 = app.channel(value_type=ProcessorInput)


if __name__ == '__main__':
    app.main()
