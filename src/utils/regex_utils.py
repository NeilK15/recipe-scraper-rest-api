import re


def get_int_from_str(string: str) -> int | None:
    result = re.search("/[0-9]/", string)
    return int(result) if result is not None else None
