import re
import sys


def main():
    ipt = "12:50 AM to 12:12 AM"
    convert(ipt)


# expected format:
#       9:00 AM to 5:00 PM
#       9 AM to 5 PM
def convert(user_input: str) -> str:
    VALIDATE_PATTERN = r"^(\d{1,2})(?::(\d{1,2}))? ([A-Z]{2}) to (\d{1,2})(?::(\d{1,2}))? ([A-Z]{2})$"
    match = re.search(VALIDATE_PATTERN, user_input)

    if not match:
        raise ValueError

    from_ = {}
    from_["hour"] = match.group(1)
    from_["minute"] = match.group(2) if match.group(2) else "0"
    from_["am_pm"] = match.group(3)

    to_ = {}
    to_["hour"] = match.group(4)
    to_["minute"] = match.group(5) if match.group(5) else "0"
    to_["am_pm"] = match.group(6)

    values_list = [from_, to_]

    # validating {hour} <= 12
    if int(from_["hour"]) > 12 or int(to_["hour"]) > 12:
        print("error")
        sys.exit()

    # validating {minute} <= 59
    if int(from_["minute"]) > 59 or int(to_["minute"]) > 59:
        print("error")
        sys.exit()

    for batch in values_list:
        # validating {minute} == 0 when {hour} == 12 PM
        # and adding 12 to {hour} to make it 24 hour format if its PM
        if batch["am_pm"] == "PM":
            if batch["hour"] == "12" and int(batch["minute"]) > 0:
                print("error")
                sys.exit()
            batch["hour"] = str(int(batch["hour"])+12)

    output_string = f"{from_['hour'].zfill(2)}:{from_['minute'].zfill(2)} to {to_['hour'].zfill(2)}:{to_['minute'].zfill(2)}"
    print(output_string)


if __name__ == "__main__":
    main()
