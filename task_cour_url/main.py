import asyncio
import requests


async def get_url(url):
    result_code = requests.get(url)
    print('get_url start')
    await asyncio.sleep(1)
    print('get_url finish')
    print(result_code.status_code)


async def get_url_2(url):
    result_code = requests.get(url)
    print('1 start')
    await asyncio.sleep(1)
    print('2 finished')
    print(result_code.status_code)


async def chain(**kwargs):
    await get_url('https://habr.com/ru/post/334970/')
    await get_url_2('https://habr.com/ru/post/334970/')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(chain())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

import time
import urllib.request
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    response = await aiohttp.request('GET', URL)
    datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    response.close()
    return datetime


async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


print('Asynchronous:')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
