import sys


def main():
    initial_string = "Adieu, adieu, to"
    names = get_names()

    if len(names) >= 1:
        if not len(names) == 1:
            for name_index in range((len(names)-1)):
                if name_index == len(names) - 2:
                    initial_string += f" {names[name_index]}"
                else:
                    initial_string += f" {names[name_index]},"
            initial_string += f" and {names[-1]}"
        else:
            initial_string += f" {names[0]}"
    else:
        sys.exit(1)

    print(f"\n\n{initial_string}")


def get_names():
    names = []

    while True:
        try:
            names.append(input("Name: ").capitalize())
        except EOFError:
            break

    return names


if __name__ == "__main__":
    main()
