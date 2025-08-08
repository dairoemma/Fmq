from config import Config
import asyncio
import uuid
import hashlib

host = Config.Host
port = Config.Port


async def client_connection():
    fmq_server = await asyncio.start_server(fmq_buffer, host, port )

    async with fmq_server:
        await fmq_server.serve_forever


async def fmq_buffer(*args) -> str:
            ...


asyncio.run(client_connection)

