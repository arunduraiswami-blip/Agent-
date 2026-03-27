import sys


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <non-negative-integer>")
        raise SystemExit(1)

    try:
        number = int(sys.argv[1])
        result = factorial(number)
    except ValueError as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)

    print(f"Factorial of {number} is {result}")


if __name__ == "__main__":
    main()
