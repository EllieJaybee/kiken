<p align="center" style="font-size: xxx-large;!important"><b>kiken</b></p><p align="center">
<hr/>
kiken is a Python wrapper for the Elite Dangerous Star Map (EDSM) API. It allows you to interact with the EDSM API asynchronously using `aiohttp`, making it easy to fetch data about systems, stations, markets, and more in the Elite Dangerous universe.
</p>

## Current Features (More soon™️!)

- Fetch system information including bodies and stations
- Retrieve market data for specific stations
- Asynchronous requests using [aiohttp](https://docs.aiohttp.org/en/stable/)
- Debug mode for saving API responses to JSON files

## Installation

```sh
pip install --upgrade git+https://github.com/EllieJaybee/kiken.git
```

## Usage

```py
import asyncio

from kiken import Client

async def main():
    client = Client()
    system = await client.get_system("Lifthruti")
    print(f"{system.body_count} bodies in {system.name}")
    for body in system.bodies:
        print(body.name)

asyncio.run(main())
```

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

This project is not affiliated with the [Elite Dangerous Star Map](https://www.edsm.net/) project.