import subprocess

def generate_keypair():
    private_key = subprocess.check_output("wg genkey", shell=True).decode().strip()
    public_key = subprocess.check_output(f"echo {private_key} | wg pubkey", shell=True).decode().strip()
    return {"private_key": private_key, "public_key": public_key}
