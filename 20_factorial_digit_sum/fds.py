import sys

def factorial(n: int) -> int:
    res = n

    for i in range(1, n):
        res *= i

    return res

def main() -> int:
    f = factorial(100)

    res = 0

    for d in str(f):
        res += int(d)

    print(res)

    return 0

if __name__ == "__main__":
    sys.exit(main())
