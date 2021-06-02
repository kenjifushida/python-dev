import aiohttp
import asyncio

from bs4 import BeautifulSoup as bs
import re

async def fetch(session, q, id = None):
    task_ids = []
    if id:
        url = f'http://web.sfc.keio.ac.jp/~husni/learn/genlinks.php?{id}'
    else:
        url = 'http://web.sfc.keio.ac.jp/~husni/learn/genlinks.php'

    async with session.get(url) as response:
        html = await response.text()
        soup = bs(html, 'html.parser')
        h3 = soup.h3.text
        id_pattern = re.compile(r'(\d+)')
        page_id = id_pattern.search(h3)
        if id != page_id.group(1):
            task_ids.append(page_id.group(1))
        p_tags = soup.find_all('p')
        for p in p_tags:
            link = p.find('a')['href']
            new_id = id_pattern.search(link)
            task_ids.append(new_id.group(1))
        await q.put(task_ids)


async def verify_url(session, q_in):
    urls = []
    tasks = []
    try:
        while True:
            ids = await q_in.get()
            for id in ids:
                if id not in urls:
                    urls.append(id)
                    tasks.append(asyncio.create_task(fetch(session, q_in, id)))
            await asyncio.gather(*tasks)
            q_in.task_done()
    except asyncio.CancelledError:
        await q_in.put(urls)


async def main():
    q = asyncio.Queue()

    async with aiohttp.ClientSession() as session:

        task = asyncio.create_task(fetch(session, q))
        verify = asyncio.create_task(verify_url(session, q))
        await task
        await q.join()
        verify.cancel()

        urls = await q.get()
        q.task_done()

        
        with open('output.txt', 'w', newline='') as file:
            for id in urls:
                file.write(f'http://web.sfc.keio.ac.jp/~husni/learn/genlinks.php?{id}\n')
        

loop = asyncio.get_event_loop()
loop.run_until_complete(main())