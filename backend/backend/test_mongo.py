import asyncio
from database.mongo import client

async def test():
    try:
        await client.admin.command("ping")
        print("MongoDB connection OK")
    except Exception as e:
        print("MongoDB connection FAILED")
        print(e)

asyncio.run(test())