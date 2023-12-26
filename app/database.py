from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    client: AsyncIOMotorClient = None

async def connect_to_mongo():
    try:
        MONGO_URL = "mongodb://admin:adminpassword@mongodb:27017/?authMechanism=DEFAULT"
        Database.client = AsyncIOMotorClient(MONGO_URL)["mydatabase"]
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

async def close_mongo_connection():
    print("Closing MongoDB connection")
    pass
    # try:
    #     if Database.client:
    #         Database.client.close()
    #         print("Closed MongoDB connection")
    # except Exception as e:
    #     print(f"Error closing MongoDB connection: {e}")
