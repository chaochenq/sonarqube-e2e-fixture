import hashlib


def fingerprint(document: bytes) -> str:
    return hashlib.md5(document).hexdigest()
