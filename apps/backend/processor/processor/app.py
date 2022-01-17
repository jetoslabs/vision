import faust

from processor.images.models import MyModel, MyModel1

app: faust.App = faust.App(
    'vision_processor',
    version=1,
    autodiscover=True,
    origin='processor'
)

channel = app.channel(value_type=MyModel)
channel1 = app.channel(value_type=MyModel1)


@app.agent(channel=channel1)
async def agent1(stream):
    async for event in stream:
        print(f"agent1 received: {str(event)}")


@app.agent(channel=channel, sink=[channel1])
async def agent0(stream):
    event: MyModel
    async for event in stream:
        print(f"agent0 received: {str(event)}")
        yield MyModel1(event.x)
        # await app.send(channel=channel1, value=MyModel1(event.x))


@app.agent()
async def agent_b(stream):
    async for event in stream:
        print(f'AGENT B RECEIVED: {event!r}')


@app.agent(channel=channel, sink=[agent_b])
async def agent_a(stream):
    async for event in stream:
        print(f'AGENT A RECEIVED: {event!r}')
        yield event


@app.timer(0.001)
async def populate():
    await channel.send(value=MyModel(303))

if __name__ == '__main__':
    app.main()
