from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import asyncio
import os

# 버거 데이터
burgers = [
    {
        "name": "빅맥",
        "price": 5500,
        "image_url": "https://example.com/images/bigmac.jpg"
    },
    {
        "name": "쿼터파운더 치즈",
        "price": 6000,
        "image_url": "https://example.com/images/quarterpounder.jpg"
    },
    {
        "name": "맥스파이시 상하이 버거",
        "price": 5800,
        "image_url": "https://example.com/images/mcspicy.jpg"
    },
    {
        "name": "1955 버거",
        "price": 6500,
        "image_url": "https://example.com/images/1955burger.jpg"
    },
    {
        "name": "더블 불고기 버거",
        "price": 5200,
        "image_url": "https://example.com/images/doublebulgogi.jpg"
    }
]

# 환경 변수 로드
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

async def insert_burgers():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[MONGO_DATABASE]
    collection = db.burgers

    # 기존 데이터 삭제 (선택사항)
    await collection.delete_many({})

    # 새 데이터 삽입
    result = await collection.insert_many(burgers)
    print(f"{len(result.inserted_ids)} 개의 문서가 삽입되었습니다.")

    # 삽입된 데이터 확인
    async for burger in collection.find():
        print(burger)

    # 연결 종료
    client.close()

# 메인 함수 실행
if __name__ == "__main__":
    asyncio.run(insert_burgers())