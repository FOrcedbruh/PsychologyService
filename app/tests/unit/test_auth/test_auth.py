import pytest
from httpx import AsyncClient
from fastapi import status
from tests.test_config import settings



class TestAuth:

    @pytest.mark.asyncio
    async def test_login(self, async_client: AsyncClient, jwt_tokens):
        res = await async_client.post(url="auth/login", json=settings)
        jwt_tokens["access_token"], jwt_tokens["refresh_token"]  = res.json()["access_token"], res.json()["refresh_token"]
        assert res.status_code == status.HTTP_200_OK


    @pytest.mark.asyncio
    async def test_me(self, async_client: AsyncClient, jwt_tokens):
        res = await async_client.get("/auth/me", headers={"Authorization": f"Bearer {jwt_tokens["access_token"]}"})
        assert res.status_code == status.HTTP_200_OK


    @pytest.mark.asyncio
    async def test_refresh(self, async_client: AsyncClient, jwt_tokens):
        res = await async_client.get("auth/refresh", headers={"Authorization": f"Bearer {jwt_tokens["refresh_token"]}"})
        assert res.status_code == status.HTTP_200_OK