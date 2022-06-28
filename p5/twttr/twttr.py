
def main():
    twtrr = "Twitter"
    print(shorten(twtrr))


def shorten(text: str) -> str:
    vowels = [v for v in "a e i o u".split()]
    vowels.extend([v.upper() for v in vowels])

    for vowel in vowels:
        text = text.replace(vowel, "")

    return text


if __name__ == "__main__":
    main()
