import sys
import csv

from attr import field


def main():

    if len(sys.argv) < 3:
        print("too few command line arguements")
        sys.exit()

    if len(sys.argv) > 3:
        print("too many command line arguements")
        sys.exit()

    if not sys.argv[1].endswith(".csv"):
        print("csv file is expected")
        sys.exit()

    if not sys.argv[2].endswith(".csv"):
        print("csv file is expected for output")
        sys.exit()

    try:
        with open(sys.argv[1]) as file:
            buffer = []
            reader = csv.DictReader(file)

            for row in reader:
                names = row["name"].split(",")
                buffer.append(
                    [names[1].strip(), names[0].strip(), row['house']])

        with open(sys.argv[2], "w") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["first_name", "last_name", "house"])

            for line in buffer:
                writer.writerow([line[0], line[1], line[2]])

    except FileNotFoundError:
        print("file not found")
        sys.exit()


if __name__ == "__main__":
    main()
