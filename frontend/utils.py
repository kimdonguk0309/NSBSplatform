from nacl import public, encoding

def generate_keypair():
    private_key = public.PrivateKey.generate()
    private_key_str = private_key.encode(encoder=encoding.Base64Encoder).decode()
    public_key_str = private_key.public_key.encode(encoder=encoding.Base64Encoder).decode()
    return {"private_key": private_key_str, "public_key": public_key_str}
