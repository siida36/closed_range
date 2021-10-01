from __future__ import annotations


class ClosedRange:
    def __init__(self, lower_endpoint: int, upper_endpoint: int):
        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

    def __repr__(self) -> str:
        return f"[{self.lower_endpoint}, {self.upper_endpoint}]"

    def is_proper_range(self):
        return self.lower_endpoint < self.upper_endpoint

    def is_included(self, x: int):
        return x >= self.lower_endpoint and x <= self.upper_endpoint

    def is_same_range(self, another_cr: ClosedRange):
        return (
            self.lower_endpoint == another_cr.lower_endpoint
            and self.upper_endpoint == another_cr.upper_endpoint
        )

    def is_included_to_another_range(self, another_cr: ClosedRange):
        return (
            self.lower_endpoint >= another_cr.lower_endpoint
            and self.upper_endpoint <= another_cr.upper_endpoint
        )
