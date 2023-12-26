from pydantic import BaseModel

class BrokerBase(BaseModel):
    personal_info: str
    branches: str
    mobile_phone: str
    email: str

class BrokerCreate(BrokerBase):
    pass