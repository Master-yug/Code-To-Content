def greet(name: str) -> str:
    """
    Greets the given name.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"

def say_goodbye(name: str) -> str:
    """
    Says goodbye to the given name.

    Args:
        name: The name to say goodbye to.

    Returns:
        A goodbye string.
    """
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(say_goodbye("World"))