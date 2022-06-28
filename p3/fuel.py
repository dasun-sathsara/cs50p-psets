def get_fraction(prompt):
    while True:
        try:
            values = [int(x) for x in input(prompt).split("/")]
            if not (values[0] <= values[1] and len(values) == 2):
                continue
            return tuple(values)
        except (ValueError, IndexError):
            pass


fraction = get_fraction("Fraction: ")
percentage = fraction[0] / fraction[1] * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{int(percentage)}%")
