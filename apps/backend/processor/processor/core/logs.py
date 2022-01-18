import uuid


async def generate_trace_id() -> uuid.UUID:
    # This function (uuid4) guarantees the random no. and doesn’t compromise with privacy.
    trace_id: uuid.UUID = uuid.uuid4()
    return trace_id
