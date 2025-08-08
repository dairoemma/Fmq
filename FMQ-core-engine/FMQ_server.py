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
    try:
            
        buffer = b''
        client = []
        status = True
        await retry_handler(client,status)
        while True:
            chunk = await reader.read(1024)

            if not chunk:
                status = False
                await retry_handler(client,status)
                break

            buffer += chunk

            if b'/n':
                break

        return buffer.decode().strip()
    
    except Exception as e:
        return {f"Error: fmq buffer failed: {str(e)}"}


async def retry_handler(client, status):
    try:
 
        if status:
            client.append("connected")
        else:
            if client:
                client.pop(0)
            client.append("disconnected") 

    except Exception as e:
        return {f"Error: Retry handler failed: {str(e)}"}

asyncio.run(client_connection)

