#!/usr/bin/env python

import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        print(f"received mssg = {message}")
        await websocket.send(message)
        print(f"sent mssg = {message}")


async def main():
    global future_stop
    future_stop = asyncio.Future()
    async with websockets.serve(echo, "localhost", 8765):
        print("in main")
        await future_stop  # runs forever because, it's value is not changing. Try setting its value to some string, which will result in stopping the main event loop.


if __name__ == "__main__":
    asyncio.run(main())
