for i in range(45):
    print(i)

print()

# This is a comment and should not be counted

print("")


def read_file(file) -> int:
    """
    hello
    """
    lines = file.readlines()
    counter = 0
    for line in lines:
        line_enhanced = line.strip().replace("/n", "")
        if line_enhanced.startswith("#") or len(line_enhanced) == 0:
            continue

        counter += 1

    return counter
