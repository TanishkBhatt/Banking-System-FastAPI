from math import pow

def compound_interest(money: float, rate: float, time: int):
    amount = money * (pow((1 + (rate/100)), time))
    return round(amount, 2)