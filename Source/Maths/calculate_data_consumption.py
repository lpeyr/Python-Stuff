import datetime
from calendar import monthrange


def main():
    total_data = float(
        input("What is the total amount of data do you have? (in GB) "))
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    num_days = monthrange(current_year, current_month)[1]
    data_consummed = total_data / num_days * datetime.datetime.now().day

    # Check if the number is an int
    if data_consummed == int(data_consummed):
        data_consummed = int(data_consummed)

    print(f"Today, you should've consumed {data_consummed} GB")


if __name__ == "__main__":
    main()
