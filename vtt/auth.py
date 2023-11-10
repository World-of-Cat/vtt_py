from dataclasses import dataclass


@dataclass
class AuthSession:
    nonce: str
    