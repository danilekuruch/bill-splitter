import argparse
from .models import Bill
from .splitter import split_with_lucky


def run_cli():
    parser = argparse.ArgumentParser(description="Bill Splitter with Lucky Friend feature")
    parser.add_argument("--total", type=float, required=True, help="Total bill amount")
    parser.add_argument("--friends", nargs="+", required=True, help="List of friends")
    parser.add_argument("--lucky", action="store_true", help="Enable lucky feature")

    args = parser.parse_args()
    bill = Bill(args.total, args.friends)

    if args.lucky:
        split, lucky = split_with_lucky(bill)
        print(f"{lucky} is the lucky one!")
    else:
        split = bill.split_equally()
        print("No one is lucky today.")

    print("Final split:")
    for friend, amount in split.items():
        print(f"{friend}: {amount}")
