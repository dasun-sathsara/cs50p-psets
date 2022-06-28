import re


def main():
    ipt = "Um, thanks, um...,"
    print(count(ipt))


def count(user_input: str) -> int:
    PATTERN = r"\bum\b"
    if results := re.findall(PATTERN, user_input, re.IGNORECASE):
        return len(results)
    else:
        return 0


if __name__ == "__main__":
    main()
