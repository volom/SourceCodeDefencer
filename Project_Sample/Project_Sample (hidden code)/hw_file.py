import marshal, zlib, base64

encoded_b = b'eJxtUs1u00AQ3lmvHcf5aSlIVIiDOUYgpOaCVAECyqFccmkFkiVkmewQIvwT1msQkXsqbxFFiiUuPAdv4SunvEIPiFmn4afC1n6zO7M7+30z+4Nd+VwaT2jkXwkkkxCzYGMhAOSSnwMwaUnxhQWWtKVDVsiWdMnayFasYoGDsGqRddFdtdGWbenJzoSf8wouPV3jkb2JZXwTHnjk79CpLnoVVHQDrXsVI7vJ2Keb+9hHZ5/JnYWQu0ur4QEnbHBtbXiP5t1jjOPMf5WpWN4Z87808ctxZHR1CUpWwk06fZ3ReT5am+A3mgWttEjeoDrYTobKolADdU9jrsMkUvm7KD6ovbxIQokTheiYvM2FoGzC8dWiChrfzaZ7BJou1rCCimlOcvhCLJuiamslpFXBCyr3MUmXhpwYXTin0wQP/Qvr/vDtGijBwK7tmZqmuhaaQrWd60jpuhXln9PxNKN1jDj7w3wDhoPqEbQNEdGw3YfG80+xxOUjaPi+NI8AzngJz9nr4ZlF3HnJFvQASk4oSmvBlk7DHs7ZlnnJS+sBO+Mf3N/77Wa/s7SbthllrZEyYub2aZS/9+fdQ/8oS2aFnqYT/wLuzt1D/6RI/Ed+Dd6Aq/aW/kDUIo0S3LYor22d6SgOnM36iuTaoj71to1nIMCFW9AFD9SeCcNTZdQq3iyerZuDpqGqZdgJP8fxYEd5xmMybIjYWzZNEtUhCPoT1CF+xFSHcZbNAtFgZ6ww0hhqUhnYBvNgTxVpWKR6Godj0hyjxlp8iqa6tsdxlmNtYSr/17/afZhksojxsSldftu0ClxOv+UK1zWzPbjxU4hd44VfD5vOUQ=='

exec(marshal.loads(zlib.decompress(base64.b64decode(encoded_b))))
    