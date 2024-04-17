#! /usr/bin/env python3

def do_calculation(x: float) -> float:
    """
    Simple example of a function that does a calculation
    """

    # 'x' must not be negative
    assert x >= 0

    return x + 1


def main():

    a = 3
    b = do_calculation(a)


if __name__ == '__main__':
    main()
