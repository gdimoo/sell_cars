from pydantic import BaseModel

class CarBase(BaseModel):
    brand: str
    model: str
    year: int
    color: str
    mileage: float

class CarCreate(CarBase):
    pass
