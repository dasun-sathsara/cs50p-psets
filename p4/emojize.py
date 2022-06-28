import emoji


def main():
    ipt = input("Input: ")
    emojized = emoji.emojize(ipt, language="alias")
    print(f"Output: {emojized}")


if __name__ == "__main__":
    main()
