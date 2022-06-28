import sys


def main():

    if len(sys.argv) < 2:
        print("too few command line arguements")
        sys.exit()

    if len(sys.argv) > 2:
        print("too many command line arguements")
        sys.exit()

    if not sys.argv[1].endswith(".py"):
        print("python file is expected")
        sys.exit()

    try:
        with open(sys.argv[1]) as file:
            print(read_file(file))
    except FileNotFoundError:
        print("file not found")
        sys.exit()


def read_file(file) -> int:
    lines = file.readlines()
    counter = 0
    for line in lines:
        line_enhanced = line.strip().replace("/n", "")
        if line_enhanced.startswith("#") or len(line_enhanced) == 0:
            continue

        counter += 1

    return counter


if __name__ == "__main__":
    main()
