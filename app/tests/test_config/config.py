from pydantic_settings import BaseSettings



LOGIN_DATA: dict = {
    "auth_date": 1736775561,
    "first_name": "_ilchpl_",
    "hash": "04945dfccfd34336067d22e91b5a73ca1cbe1c05c0cad04c1584b77f8d06bb1c",
    "id": 1498637315,
    "photo_url": "https://t.me/i/userpic/320/SRix9PPUznu5L0PM972gWwOf95t1NoO_h8rfOPVcZ3Y.jpg",
    "username": "ilchpl"
}

class Settings(BaseSettings):
    login_data: dict = LOGIN_DATA


settings = Settings()