import datetime
from calendar import monthrange


def main():
    total_data = int(
        input("What is the total amount of data do you have? (in GB) "))
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    num_days = monthrange(current_year, current_month)[1]
    data_consummed = total_data / num_days * datetime.datetime.now().day

    print(f"Today, you should've consumed {int(data_consummed)} GB")


if __name__ == "__main__":
    main()
