import asyncio
import websockets
import aiohttp
import time

url = 'https://newsapi.org/v2/top-headlines?country=ru&apiKey=7ef9503baea4428b9816689d82f0bc1c'
tasks =[]



async def fetch_news(url, session):  
    async with session.get(url) as response:
        data = await response.json()
        return data["articles"]
        




async def server(websocket, path):

    connected = set()
    print('received')
    while True:
        
        connected.add(websocket)

        try:
            for conn in connected:
                print(conn)
                if tasks:
                    for task in tasks:
                        to_send = task["title"] + '\n' + task["url"] +'\n\n'
                        await conn.send(to_send)
        finally:
        # Unregister.
            connected.remove(websocket)



        async with aiohttp.ClientSession() as session:            
            print('in session')
            articles = await fetch_news(url, session)
            count = 0
            for article in articles:
                if article not in tasks:
                    if count <=10:
                        tasks.append(article)
                        count += 1
                    else:
                        tasks.pop(0)
                        # print(*tasks)
            time.sleep(60)
        
        
        
        



async def main():
    async with websockets.serve(server, "localhost", 8080):
        await asyncio.Future()  # run forever
    

if __name__ == "__main__":
    asyncio.run(main())
    