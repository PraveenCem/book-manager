from app.core.database import db
import asyncio

# async def create_index():
#     result = await db.db["books"].create_index("author")
#     print("created index",result)

# asyncio.run(create_index())

# async def show_indexes():
#     indexes = await db.db["books"].index_information()
#     print(indexes)

# asyncio.run(show_indexes())

async def check_query():
    # result = await db.db["books"].find(
    #     {"author":"Praveen"}
    # ).explain()

    result = await db.db["books"].find(
        {"year":2025}
    ).explain()

    print(result)

asyncio.run(check_query())