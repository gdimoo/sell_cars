from fastapi import APIRouter, HTTPException, Depends
from models.broker import BrokerBase, BrokerCreate
from app.database import Database, close_mongo_connection, connect_to_mongo
from fastapi.responses import JSONResponse
from bson import ObjectId

router = APIRouter()

async def get_database():
    db = Database()
    try:
        await connect_to_mongo()
        yield db
    finally:
        close_mongo_connection()
        
@router.post("/", response_model=BrokerBase)
async def create_broker(broker: BrokerCreate, db: Database = Depends(get_database)):

    if db.client is None:
        return JSONResponse(content={"error": "MongoDB connection not established"}, status_code=500)

    result = await db.client.brokers.insert_one(broker.dict())

    return {**broker.dict(), "id": str(result.inserted_id)}

@router.get("/{broker_id}", response_model=BrokerBase)
async def read_broker(broker_id: str, db: Database = Depends(get_database)):
    
    broker = await db.client.brokers.find_one({"_id": ObjectId(broker_id)})

    
    if not broker:
        raise HTTPException(status_code=404, detail="Broker not found")

    
    return BrokerBase(**broker)

@router.put("/{broker_id}", response_model=BrokerBase)
async def update_broker(broker_id: str, broker: BrokerCreate, db: Database = Depends(get_database)):
    
    updated_broker_dict = broker.dict()

    
    result = await db.client.brokers.update_one(
        {"_id": ObjectId(broker_id)},
        {"$set": updated_broker_dict}
    )

    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Broker not found")

    
    return {**broker.dict(), "id": broker_id}

@router.delete("/{broker_id}", response_model=BrokerBase)
async def delete_broker(broker_id: str, db: Database = Depends(get_database)):
    
    result = await db.client.brokers.delete_one({"_id": ObjectId(broker_id)})

    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Broker not found")

    
    return {"id": broker_id}