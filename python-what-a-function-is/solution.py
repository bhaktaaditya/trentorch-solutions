def is_even(n: int) -> bool:
    return not bool(n%2)


def greet_formal(name: str, title: str) -> str:
    return f"Good day, {title} {name}."


def apply_twice(func, value):
    return func(func(value))
