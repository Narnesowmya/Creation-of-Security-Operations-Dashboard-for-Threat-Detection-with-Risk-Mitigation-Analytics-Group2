import asyncio
from database.mongo import api_keys_collection

async def main():
    docs = await api_keys_collection.find(
        {},
        {"_id": 0, "name": 1, "created_at": 1, "revoked": 1}
    ).to_list(length=10)

    for doc in docs:
        print(doc)

asyncio.run(main())