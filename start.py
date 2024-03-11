import aiohttp
import asyncio
from time import time

async def fetch(s,urls):
        msg = "Testing"
        post_url = 'https://graph.facebook.com/170398566149584_122117719106100172/comments'
        payload = {
            'message': msg,
            'access_token': 'EAAJaFzIvewkBOz6v1eiqsZBkmuMG6SBINhZC88H38n7YCefoiRbFZCwG7aJz1RbgJHkQupU3ZCMrBIX8LXYL7XxP8VPBBQmbipGGZBYP8GEeelY2tRWFgUtKlkvPFN1xyCZBmcMgidSZBd84XZClBxrlycSo1mFPfezQpjZBFUv2ayISOVbQMHIa0lXuCGWT9HusZD',
    }
        async with s.post(post_url, data=payload) as r:
                if r.status != 200:
                        r.raise_for_status()
                return await r.text()

async def fetch_all(s, urls):
        tasks = []
        for url in urls:
                task = asyncio.create_task(fetch(s, url))
                tasks.append(task)
        res = await asyncio.gather(*tasks)
        return res

async def main():
        urls = range(1, 100)
        async with aiohttp.ClientSession() as s:
                htmls = await fetch_all(s,urls)
                print(htmls)


def zahid():
        try:
                start = time()
                asyncio.run(main())
                stop = time()
                print("time taken:",stop-start)
                zahid()
        except Exception as e:
                print(e)
                zahid()
zahid()
