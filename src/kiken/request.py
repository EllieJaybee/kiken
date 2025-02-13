import aiohttp
import asyncio
import json
import os


class Request:
    def __init__(self, is_debug: bool = False) -> None:
        self.backoff = False
        self.is_debug = is_debug

    async def request(self, endpoint: str, **params) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://www.edsm.net/{endpoint}", params=params
            ) as response:
                response_text = await response.text()
        jsonmsg = json.loads(response_text)
        if self.is_debug:
            os.makedirs("tests", exist_ok=True)
            with open(f"tests/{endpoint.split('/')[-1]}.json", "w") as f:
                json.dump(jsonmsg, f, indent=4)
        ratelimit = int(response.headers["X-Rate-Limit-Remaining"])
        if ratelimit is None:
            print("Ratelimit is Nonetype")
        if ratelimit < 360:
            self.backoff = True
        elif ratelimit == 720:
            self.backoff = False
        if self.backoff:
            await asyncio.sleep(10)
        return jsonmsg
