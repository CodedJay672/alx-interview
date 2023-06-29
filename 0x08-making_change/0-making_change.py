#!/usr/bin/python3
""" making change module """


def makeChange(coins, total):
    """
    This function calculates the minimum number of coins needed
    to reach the total amount

    """
    if total <= 0:
        return 0
    else:
        # Sort the coins in descending order
        coin = sorted(coins, reverse=True)
        counter = 0
        # Iterate through the coins and subtract them from the total
        for i in coin:
            while total >= i:
                counter += 1
                total -= i
        # If the total amount is reduced to zero, return the counter
        if total == 0:
            return counter
        # If the total amount cannot be reached with the given coins, return -1
        return -1
