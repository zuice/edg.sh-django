def str_to_bool(value: str) -> bool:
    return value.lower() in ("true", "yes", "1", "on")
