def birthday_problem(number_of_days_year: int, n: int) -> float:
    """In probability theory, the birthday problem asks for the probability
    that, in a set of n randomly chosen people, at least two will
    share a birthday.

    Args:
        number_of_days_year (int): Number of days in a year 
                                    (custom to increase the sample space)
        n (int): number of people

    Returns:
        float: returns the percentage at least two will share a birthday
    """    
    # compute probability no two share the same birthday
    prob = 100.0
    if (n > number_of_days_year):
        return prob

    while (n > 0):
        prob *= (number_of_days_year-n+1)/number_of_days_year
        n -= 1

    return round(100-prob, 2)
    

def binary_search(number_of_days_year:int, low: int, high: int
                , threshold: float):
    """Implements the binary search algo to find the minimum number of
    individuals required for which the probability atleast two persons
    share same birthday exceeds threshold (birthdayParadox)

    Args:
        number_of_days_year (int): Number of days in a year
                                    (custom to increase the sample space)
        low (int): lower bound of search space
        high (int): upper bound of search space

    Returns:
        int: returns the minimum number of persons required to have
                birthdayProblem greater than threshold
    """
    if (low >= high):
        return high
    mid = low + (high - low)//2
    prob = birthday_problem(number_of_days_year, mid)
    if (prob < threshold):
        low = mid + 1
    else:
        high = mid
    return binary_search(number_of_days_year, low, high, threshold)


def birthday_paradox(number_of_days_year: int) -> int:
    """Find the minimum number of individual required
    for which the probability atleast two persons share same birthday
    exceeds 50% (birthdayParadox)

    Args:
        number_of_days_year (int): Number of days in a year
                                    (custom to increase the sample space)

    Returns:
        int: returns the minimum number of persons required to have
                birthdayProblem greater than 50%
    """
    low, high = 1, number_of_days_year
    threshold = 50
    return binary_search(number_of_days_year, low, high, threshold)


if __name__ == "__main__":
    number_of_days_year = int(input("Enter number of days in your custom year: "))
    n = int(input("Enter number of random persons: "))
    print(birthday_problem(number_of_days_year, n))
    print(birthday_paradox(number_of_days_year))
