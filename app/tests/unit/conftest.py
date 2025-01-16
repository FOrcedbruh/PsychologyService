import pytest_asyncio
from httpx import AsyncClient
from config import settings



@pytest_asyncio.fixture(autouse=True)
async def async_client():
    async with AsyncClient(base_url=f"http://localhost:{settings.run.port}/api/v1") as client:
        yield client


@pytest_asyncio.fixture(scope="session")
async def jwt_tokens():
    return {
        "access_token": "",
        "refresh_token": ""
    }