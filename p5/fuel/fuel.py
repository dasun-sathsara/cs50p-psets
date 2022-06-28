def main():
    perc = convert("1/5")
    print(guage(perc))


def convert(prompt: str) -> int:
    try:
        values = [int(x) for x in prompt.split("/")]
        if values[1] == 0:
            raise ZeroDivisionError
        assert values[0] <= values[1] and len(values) == 2

        return int(values[0] / values[1] * 100)

    except (TypeError, AssertionError):
        raise ValueError


def guage(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
