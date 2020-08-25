import threading
from multiprocessing import Pool
import asyncio
import aiohttp
from tortoise import run_async
from tortoise import Tortoise
from demo_project.models import *
import nest_asyncio
import random

nest_asyncio.apply()


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models' : ['demo_project.models']}
    )

    await Tortoise.generate_schemas()


    async def get_response(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response


    links_container = await Links.all()

    for link in links_container:
        for _ in range(random.randint(2, 10)):
            coroutines = [get_response(str(link))]

            loop = asyncio.get_event_loop()

            result = loop.run_until_complete(asyncio.gather(*coroutines))

            await Answers_On_Requests(body=str(result), link_id=link.id).save()




if __name__ == "__main__":
    run_async(init())




