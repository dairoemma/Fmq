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


async def fmq_buffer(reader):
    buffer = b''

    while True:
        chunk = await reader.read(1024)

        if not chunk:
            break

        buffer += chunk

        if b'/n':
            break

    return buffer.decode().strip()


asyncio.run(client_connection)

