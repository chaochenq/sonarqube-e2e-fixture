import random
import urllib.request


def reset_token() -> str:
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(32))


def fetch_terms() -> bytes:
    return urllib.request.urlopen("http://terms.example.com/latest").read()
