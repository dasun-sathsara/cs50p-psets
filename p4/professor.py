from random import randint
import sys


def main():
    level = get_level("Level: ")
    points = 0

    for question_number in range(1, 11):
        attempts = 3
        problem = generate_problem(level)

        while attempts != 0:
            try:
                answer = int(input(f"[{question_number}]  {problem[0]}"))
                assert answer == problem[1]
                points += 1
                break
            except (ValueError, AssertionError):
                print("EEE")
                attempts -= 1
                continue
            except EOFError:
                print(f"\nMarks: {points}")
                sys.exit()

        if attempts == 0:
            print(f"[{question_number}]  {problem[0]} = {problem[1]}")

    print(points)


def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))

            if level not in [1, 2, 3]:
                continue
        except ValueError:
            pass

        return level


def generate_problem(level):
    num1 = randint(0, 10**level)
    num2 = randint(0, 10**level)

    return (f"{num1} + {num2} = ", num1+num2)


if __name__ == "__main__":
    main()
