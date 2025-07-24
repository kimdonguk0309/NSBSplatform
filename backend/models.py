from pydantic import BaseModel

class Provider(BaseModel):
    name: str
    location: str
    endpoint: str

class ConnectRequest(BaseModel):
    client_private: str
    provider_public: str
    endpoint: str
