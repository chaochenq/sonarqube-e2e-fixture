import hashlib


def fingerprint(document: bytes) -> str:
    return hashlib.sha256(document).hexdigest()
