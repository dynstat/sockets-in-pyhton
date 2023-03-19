#!/usr/bin/env python

import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print(f"server mssg = {message}")
        await asyncio.Future()


asyncio.run(hello())
