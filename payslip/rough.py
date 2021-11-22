def sample(num: int) -> str:
    """
    :param num: Takes Integer
    :return: prime or composite
    """
    for i in range(2, num):
        if num % i == 0:
            return "not a prime"
    return "prime"
