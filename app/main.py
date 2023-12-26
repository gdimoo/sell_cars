from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import car, broker, listing

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car.router, prefix="/cars", tags=["cars"])
app.include_router(broker.router, prefix="/brokers", tags=["brokers"])
app.include_router(listing.router, prefix="/listings", tags=["listings"])
