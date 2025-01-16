import pytest
from httpx import AsyncClient
from fastapi import status




class TestAuth:

    @pytest.mark.asyncio
    async def test_login(self, async_client: AsyncClient, jwt_tokens):
        data_to_login: dict = {
            "auth_date": 1736775561,
            "first_name": "_ilchpl_",
            "hash": "04945dfccfd34336067d22e91b5a73ca1cbe1c05c0cad04c1584b77f8d06bb1c",
            "id": 1498637315,
            "photo_url": "https://t.me/i/userpic/320/SRix9PPUznu5L0PM972gWwOf95t1NoO_h8rfOPVcZ3Y.jpg",
            "username": "ilchpl"
        }
        res = await async_client.post(url="auth/login", json=data_to_login)
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