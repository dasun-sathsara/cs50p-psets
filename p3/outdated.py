def main():
    date = get_date()

    # * Formatting the date in standard format YYYY-MM-DD
    print(f"{date[0]}-{date[1].zfill(2)}-{date[2].zfill(2)}")


# // trying to get a date text formatted like this: 9/8/1636 OR September 8, 1636
def get_date():
    MONTHS = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    while True:
        date = input("Date: ")
        number_format = False

        # * trying to get the date as: 9/8/1636
        try:
            date_list = [x.strip() for x in date.split("/")]
            month, day, year = date_list
            number_format = True
        except ValueError:  # * trying to get the date as: September 8, 1636
            try:
                date_list = [x.strip() for x in date.split(",")]
                month_day, year = date_list
                month, day = month_day.split()
            except ValueError:  # * handle all other input errors
                continue
        except Exception:
            continue

        # * checking validity of date and year
        try:
            assert int(day) <= 31 and int(day) > 0
            assert len(year) <= 4 and int(year) > 0
        except (AssertionError, ValueError):
            continue

        # * if the input format was number format -> check for validity of month as follows
        if number_format:
            try:
                assert int(month) <= 12 and int(month) > 0
            except AssertionError:
                continue
        else:  # * checking for validity of months if it's in word form
            try:
                assert month.capitalize() in MONTHS
            except AssertionError:
                continue

            # * month name -> month number
            month = MONTHS.index(month.capitalize()) + 1

        return (str(year), str(month), str(day))


if __name__ == "__main__":
    main()
