import os
import subprocess
import base64

def generate_keypair():
    private_key = subprocess.check_output("wg genkey", shell=True).decode().strip()
    public_key = subprocess.check_output(f"echo {private_key} | wg pubkey", shell=True).decode().strip()
    return {"private_key": private_key, "public_key": public_key}

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
