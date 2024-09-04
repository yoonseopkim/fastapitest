from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

# URL에 이미 사용자 이름과 비밀번호가 포함되어 있으므로 추가 대체 필요 없음
client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DATABASE]

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await client.server_info()

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

async def get_all_burgers():
    burger_collection = db.burgers
    burgers = await burger_collection.find().to_list(1000)
    return burgers

@app.get("/burgers")
async def read_burgers():
    burgers = await get_all_burgers()
    return {"burgers": burgers}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)