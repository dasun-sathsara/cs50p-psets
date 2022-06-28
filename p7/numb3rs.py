import re
import sys


def main():
    check_args()
    address = sys.argv[1].strip()
    print(validate(address))


def validate(address: str) -> bool:
    pattern = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
    if results := re.findall(pattern, address):
        for octet in results[0]:
            if int(octet) > 255:
                return False
        else:
            return True
    else:
        return False


def check_args():
    if len(sys.argv) < 2:
        print("too few command line arguements")
        sys.exit()

    if len(sys.argv) > 2:
        print("too many command line arguements")
        sys.exit()

    return True


if __name__ == "__main__":
    main()
