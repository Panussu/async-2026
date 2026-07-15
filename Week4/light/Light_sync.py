import asyncio
import httpx
from time import time


BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6710301011"

LIGHTS = [
    "light_1",
    "light_2",
    "light_3",
    "light_4"
]


async def reset_lights(client: httpx.AsyncClient):
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/reset"

    print("Resetting all lights to OFF...")

    response = await client.delete(url)
    response.raise_for_status()

    print("All lights have been reset to OFF.\n")


async def turn_on_light(
    client: httpx.AsyncClient,
    light_id: str
):
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    payload = {"status": "ON"}

    print(f"Turning on {light_id}...")

    response = await client.post(
        url,
        json=payload
    )

    response.raise_for_status()

    result = response.json()

    print(
        f"{result.get('light_id', light_id)} is now "
        f"{result.get('current_status', 'ON')}"
    )


async def main():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            await reset_lights(client)

            print("========================================")
            print("--- Sequential Light Control ---")
            print("========================================")

            start_time = time()

            # Each light waits for the previous light
            for light_id in LIGHTS:
                await turn_on_light(client, light_id)

            elapsed = time() - start_time

            print(
                f"\nSequential total time: "
                f"{elapsed:.2f} seconds"
            )

    except httpx.ConnectError:
        print(f"Cannot connect to server: {BASE_URL}")

    except httpx.HTTPStatusError as error:
        print(
            f"HTTP error {error.response.status_code}: "
            f"{error.response.text}"
        )

    except httpx.RequestError as error:
        print(f"Request error: {error}")


if __name__ == "__main__":
    asyncio.run(main())