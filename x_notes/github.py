from typing import Tuple
from base64 import b64encode
from os import environ
from nacl import encoding, public
import requests


_base_url = f"https://api.github.com/repos/{environ['REPO']}/actions/secrets"
_headers = {
    "Authorization": f"Bearer {environ['GH_TOKEN']}",
}


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a string using a public key"""
    public_key = public.PublicKey(public_key.encode(), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode())
    return b64encode(encrypted).decode()


def get_public_key() -> Tuple[str, str]:
    url = f"{_base_url}/public-key"
    resp = requests.get(url, headers=_headers)
    resp.raise_for_status()
    j = resp.json()
    return j["key"], j["key_id"]


def update_secret(secret_key: str, secret_value: str) -> None:
    public_key, key_id = get_public_key()
    url = f"{_base_url}/{secret_key}"
    payload = {
        "encrypted_value": encrypt(public_key, secret_value),
        "key_id": key_id,
    }
    resp = requests.put(url, headers=_headers, json=payload)
    resp.raise_for_status()
