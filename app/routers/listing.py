from fastapi import APIRouter, HTTPException, Depends
from models.listing import ListingBase, ListingCreate
from app.database import Database, close_mongo_connection, connect_to_mongo

router = APIRouter()

def get_database():
    db = Database()
    try:
        connect_to_mongo()
        yield db
    finally:
        close_mongo_connection()
        
@router.get("/{car_id}", response_model=ListingBase)
async def get_car_status(car_id: str, db: Database = Depends(get_database)):
    
    listing = await db.client.sell_cars.listings.find_one({"car_id": car_id})

    
    if not listing:
        raise HTTPException(status_code=404, detail="Car listing not found")

    
    return ListingBase(**listing)