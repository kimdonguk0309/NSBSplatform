# wireguard.py 대체 예시
import nacl.public
import base64

def generate_keypair():
    private_key = nacl.public.PrivateKey.generate()
    public_key = private_key.public_key
    private_key_b64 = base64.b64encode(bytes(private_key)).decode('ascii')
    public_key_b64 = base64.b64encode(bytes(public_key)).decode('ascii')
    return {"private_key": private_key_b64, "public_key": public_key_b64}

def build_client_config(data):
    config = f"""
[Interface]
PrivateKey = {data.client_private}
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = {data.provider_public}
Endpoint = {data.endpoint}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
    return {"wg_config": config}
