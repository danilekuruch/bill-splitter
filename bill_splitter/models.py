from typing import List, Dict


class Bill:
    """Represents a bill to be split among friends."""

    def __init__(self, total: float, friends: List[str]):
        if total <= 0:
            raise ValueError("Bill amount must be positive")
        if not friends:
            raise ValueError("At least one friend required")

        self.total = total
        self.friends = friends

    def split_equally(self) -> Dict[str, float]:
        """Split the bill equally among friends."""
        share = round(self.total / len(self.friends), 2)
        return {friend: share for friend in self.friends}
