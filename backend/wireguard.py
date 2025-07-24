# wireguard.py 대체 예시
import nacl.public
import base64

def generate_keypair():
    private_key = nacl.public.PrivateKey.generate()
    public_key = private_key.public_key
    private_key_b64 = base64.b64encode(bytes(private_key)).decode('ascii')
    public_key_b64 = base64.b64encode(bytes(public_key)).decode('ascii')
    return {"private_key": private_key_b64, "public_key": public_key_b64}
