from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend import wireguard, models, database

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def register_provider(data: models.Provider):
    wg_key = wireguard.generate_keypair()
    provider = data.dict()
    provider.update(wg_key)
    database.add_provider(provider)
    return {"message": "Registered", "public_key": wg_key["public_key"]}

@app.get("/providers")
async def list_providers():
    return database.get_providers()

@app.post("/connect")
async def connect_to_provider(data: models.ConnectRequest):
    return wireguard.build_client_config(data)
