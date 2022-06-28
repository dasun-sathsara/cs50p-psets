def contain_digits(word: str):
    # Return True if the string contains any numeric characters
    for char in word:
        if char.isdigit():
            return True
    else:
        return False


def get_index_fdigit(word: str):
    # Returns the index of the first digit
    for i, char in enumerate(word):
        if char.isdigit():
            return i


def check_digits(word: str):
    # Returns True if all the characters are numeric characters

    index = get_index_fdigit(word)
    for char in word[index:]:
        if not char.isdigit():
            return False
    return True


def is_valid(word: str):
    checks = {}
    checks["two_char_check"] = True
    checks["length_check"] = True
    checks["middle_number_check"] = True
    checks["first_no_zero_check"] = True
    checks["no_punc_check"] = True

    # Checks if the length is greater than 6
    if not (len(word) <= 6 and len(word) >= 2):
        checks["length_check"] = False

    # Checks if first two characters are letters
    if len(word) >= 2:
        if not (word[0].isalpha() and word[1].isalpha()):
            checks["two_char_check"] = False

    # Checks for letter after first number
    if contain_digits(word):
        if not check_digits(word):
            checks["middle_number_check"] = False

    # Check if the first digit is 0
    if contain_digits(word):
        if word[get_index_fdigit(word)] == "0":
            checks["first_no_zero_check"] = False

    if not word.isalnum():
        checks["no_punc_check"] = False

    # Returns True if all the checks are validated
    if False in checks.values():
        return False
    else:
        return True

    # return checks


def main():
    user_input = "555"
    checks = is_valid(user_input)
    if checks:
        print("VALID")
    else:
        print("INVALID")

    # for check, status in checks.items():
    #     print(f"{check} --> {status}")


main()

word = "hello"
word.isalnum()
