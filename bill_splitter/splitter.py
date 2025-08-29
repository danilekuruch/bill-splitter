import random
from models import Bill


def split_with_lucky(bill: Bill) -> tuple[dict[str, float], str]:
    """Split the bill but make one lucky person pay nothing."""
    lucky_friend = random.choice(bill.friends)
    split = {}

    for friend in bill.friends:
        if friend == lucky_friend:
            split[friend] = 0.0
        else:
            split[friend] = round(bill.total / (len(bill.friends) - 1), 2)

    return split, lucky_friend
