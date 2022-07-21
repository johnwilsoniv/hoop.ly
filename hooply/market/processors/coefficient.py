from hooply.market.processors import START_POS, END_POS
from decimal import Decimal

class Coefficient:
    def __init__(self, start, end, linear=True):
        if end is None:
            end = start

        p1 = (START_POS, start)
        p2 = (END_POS, end)

        self.slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.b = p2[1] - self.slope * p2[0]

    def get_coefficient(self, pos: float) -> Decimal:
        if pos < START_POS or pos > END_POS:
            exit(1)
        return round(Decimal(self.slope * pos + self.b), 2)
