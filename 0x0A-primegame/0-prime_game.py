#!/usr/bin/python3

""" prime  game module """

def isWinner(x, nums):
    """
    This function returns the winner in the prime game
      The game runs for x rounds and players have to choose
      prime numbers from the argument 'nums' which is an array
      of consecutive integers, the player get to pick both the
      prime number and its multiple from the array.

    """

    def getPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to get the next prime number greater than or equal to 'num'
    def getNextPrime(num):
        while True:
            num += 1
            if getPrime(num):
                return num

    # Function to determine the winner of a single game
    def getWinner(n):
        # Maria wins if 'n' is 1 since there are no prime numbers to choose
        if n == 1:
            return "Maria"

        # Initialize a list to keep track of removed numbers
        removed = [False] * (n + 1)

        # Find the next prime number and remove it and its multiples
        prime = 2
        while prime <= n:
            for i in range(prime, n + 1, prime):
                removed[i] = True
            prime = getNextPrime(prime)

        # Count the number of removed prime numbers
        maria_count = sum(removed[i] for i in range(2, n + 1, 2))
        ben_count = sum(removed[i] for i in range(3, n + 1, 2))

        # Determine the winner based on the count of removed primes
        if maria_count > ben_count:
            return "Maria"
        elif ben_count > maria_count:
            return "Ben"
        else:
            return None

    # Count the wins for each player
    maria_wins = 0
    ben_wins = 0

    # Play each round and update the win counts
    for n in nums:
        winner = getWinner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

