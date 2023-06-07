from random import randint

from lexicon.lexicon import gener_chars, chars_s


def generate_password(length: int) -> str:
    if length < 8:
        password = f'Password is not currently from {length} chars.'
        return password
    cnt = 0
    password_l: list[str] = []
    while cnt != length:
        c = chars_s[randint(0, len(chars_s))]
        if c in gener_chars['not_used']:
            continue
        password_l.append(c)
        cnt += 1
    password = ''.join(password_l)
    return password
