import asyncio
import websockets

tasks =['news1', 'news2', 'news3']
connected = set()

async def server(websocket, path):

    await websocket.recv()
    await websocket.send('news')



async def main():
    async with websockets.serve(server, "localhost", 8080):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())