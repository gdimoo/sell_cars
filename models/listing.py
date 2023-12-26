from pydantic import BaseModel
from enum import Enum

class ListingBase(BaseModel):
    class ListingStatus(str, Enum):
        INACTIVE = 'inactive'
        ACTIVE = 'active'
        SOLD = 'sold'

    status: ListingStatus

class ListingCreate(ListingBase):
    pass
