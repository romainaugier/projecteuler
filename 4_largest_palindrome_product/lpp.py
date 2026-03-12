import sys

def is_palindrome(num: int) -> bool:
    num_str = str(num)

    num_str_sz = len(num_str)

    if num_str_sz % 2 == 0:
        return list(num_str[:num_str_sz // 2]) == list(reversed(num_str[num_str_sz // 2:]))
    else:
        return list(num_str[:num_str_sz // 2]) == list(reversed(num_str[num_str_sz // 2 + 1:]))

def main() -> int:
    palindromes = list()

    for x in range(999, 1, -1):
        for y in range(999, 1, -1):
            z = x * y

            if is_palindrome(z):
                palindromes.append(z)
                print(z, x, y)

    print(max(palindromes))

    return 0

if __name__ == "__main__":
    sys.exit(main())
