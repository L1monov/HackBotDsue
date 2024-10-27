from typing import List, Union, Dict

import aiomysql

from config import DB_LOGIN, DB_PASSWORD, DB_PORT, DB_HOST, DB_NAME

class AsyncDataBase:

    def __init__(self):
        self.pool = None

    async def init(self):
        if not self.pool:
            self.pool = await aiomysql.create_pool(
                host=DB_HOST,
                port=int(DB_PORT),
                user=DB_LOGIN,
                password=DB_PASSWORD,
                db=DB_NAME,
                cursorclass=aiomysql.DictCursor,
            )

    async def close(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    async def execute_query_for_gpt(self, query: str):
        await self.init()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query)
                result = await cursor.fetchall()
                return result

    async def execute_query(self, query: str, args: tuple = ()) -> Union[None, List]:
        await self.init()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, args)
                await conn.commit()
                result = await cursor.fetchall()
                return result



class Helpful(AsyncDataBase):
    pass