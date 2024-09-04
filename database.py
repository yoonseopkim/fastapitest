from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

# URL에서 username과 password 부분을 실제 값으로 대체
MONGO_URL = MONGO_URL.replace("<db_username>", MONGO_USERNAME).replace("<db_password>", MONGO_PASSWORD)

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DATABASE]

async def get_all_burgers():
    burger_collection = db.burgers
    burgers = await burger_collection.find().to_list(1000)
    return burgers

# 여기에 필요한 다른 데이터베이스 관련 함수들을 추가할 수 있습니다.