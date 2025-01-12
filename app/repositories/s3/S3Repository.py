from aiobotocore.session import get_session, AioSession, AioBaseClient
from contextlib import asynccontextmanager
from datetime import datetime
from config import settings
from botocore.exceptions import ClientError

class S3Repository():

    def __init__(
        self, 
        access_key: str,
        secret_key: str,
        storage_url: str,
        bucket_name: str
    ):
        self.config: dict = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": storage_url
        }
        self.bucket_name: str = bucket_name
        self.session: AioSession = get_session()
    

    @asynccontextmanager
    async def connection(self) -> AioBaseClient:
        async with self.session.create_client("s3", **self.config) as connector:
            yield connector


    async def upload_object(self, file) -> str:
        content = await file.read()
        filename: str = str(datetime.now()).replace(" ", "") + file.filename
        try:
            async with self.connection() as c:
                await c.put_object(Key=filename, Body=content, Bucket=self.bucket_name)
        except ClientError as e:
            raise e
        return settings.s3.get_url + "/" + filename

    
    async def delete_object(self, filename) -> None:
        try:
            async with self.connection() as c:
                await c.delete_object(Key=filename, Bucket=self.bucket_name)
        except ClientError as e:
            raise e
        

    async def delete_objects(self, filenames: list[str]) -> None:
        objects_to_delete: list[dict] = []
        for filename in filenames:
            objects_to_delete.append({"Key": filename})
        async with self.connection as c:
            await c.delete_objects(Bucket=self.bucket_name, Delete={"Objects": objects_to_delete})


    async def upload_objects(self, files) -> None:
        async with self.connection as c:
            for file in files:
                content = file.read()
                filename: str = file.filename + datetime.now()
                await c.put_objects(Key=filename, Bucket=self.bucket_name, Body=content)