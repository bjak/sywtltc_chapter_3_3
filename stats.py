"""Some simple statistical functions."""
import numbers
import collections

def mean(data):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'. See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    pass

def median(numbers):
    """Finds the median or middle of a list of sorted numbers, a simple measure of 'middle'. See: https://en.wikipedia.org/wiki/Median"""
    assert len(numbers) > 3, 'Length of Numbers Must be more than 3'
    assert isinstance(numbers, collections.Iterable), 'Is Iterable' 
    numbers = sorted(numbers)
    center = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return sum(numbers[center - 1:center + 1]) // 2
    else:
        return numbers[center]
    pass

def range(numbers):
    """Finds ths range of a list of numbers, a simple measure of variance. See: https://www.mathsisfun.com/definitions/range-statistics-.html"""
    pass

def standard_deviation(numbers):
    """Finds the standard deviation of a list of numbers, a measure of variance. See: https://www.mathsisfun.com/data/standard-deviation-formulas.html"""
    pass
