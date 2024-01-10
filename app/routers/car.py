from fastapi import APIRouter, HTTPException, Depends
from models.car import CarBase, CarCreate
from app.database import Database, close_mongo_connection, connect_to_mongo
from bson import ObjectId

router = APIRouter()

async def get_database():
    db = Database()
    try:
        await connect_to_mongo()
        yield db
    finally:
        close_mongo_connection()

@router.post("/", response_model=CarBase)
async def create_car(car: CarCreate, db: Database = Depends(get_database)):
    
    car_dict = car.dict()

    
    result = await db.client.cars.insert_one(car_dict)

    
    return {**car.dict(), "id": str(result.inserted_id)}

@router.get("/{car_id}", response_model=CarBase)
async def read_car(car_id: str, db: Database = Depends(get_database)):
    
    car = await db.client.cars.find_one({"_id": ObjectId(car_id)})

    
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    
    return CarBase(**car)

@router.put("/{car_id}", response_model=CarBase)
async def update_car(car_id: str, car: CarCreate, db: Database = Depends(get_database)):
    
    updated_car_dict = car.dict()

    result = await db.client.cars.update_one(
        {"_id": ObjectId(car_id)},
        {"$set": updated_car_dict}
    )

    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")

    
    return {**car.dict(), "id": car_id}

@router.delete("/{car_id}", response_model=CarBase)
async def delete_car(car_id: str, db: Database = Depends(get_database)):
    
    result = await db.client.cars.delete_one({"_id": ObjectId(car_id)})

    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")

    
    return {"id": car_id}