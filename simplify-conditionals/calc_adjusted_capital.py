# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace nested conditional with guard clauses.

ADJ_FACTOR = 0.7
def all_greater_than_0(capital, rate, duration):
    return capital > 0 and rate > 0 and duration > 0

def get_adjusted_capital(capital, rate, duration, income):
    result = 0
    if all_greater_than_0:
        result = (income / duration) * ADJ_FACTOR
    return result

adjusted_capital = get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital)
