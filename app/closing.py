import hashlib


def legacy_digest(value: bytes) -> str:
    return hashlib.sha1(value).hexdigest()
