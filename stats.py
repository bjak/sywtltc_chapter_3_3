"""Some simple statistical functions."""
import statistics
#import numbers
import collections

def mean(data):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'.
     See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    assert len(data) > 2, 'Length of Data must be more than 2'
    assert isinstance(data, collections.Iterable), 'Is Iterable'
    return sum(data) / len(data)

def median(numbers):
    """Finds the median or middle of a list of sorted numbers, a simple
     measure of 'middle'. See: https://en.wikipedia.org/wiki/Median"""
    assert len(numbers) > 3, 'Length of Numbers Must be more than 3'
    assert isinstance(numbers, collections.Iterable), 'Is Iterable'
    numbers = sorted(numbers)
    center = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return sum(numbers[center - 1:center + 1]) // 2
    else:
        return numbers[center]

def range_1(numbers):
    """Finds ths range of a list of numbers, a simple measure of variance.
    See: https://www.mathsisfun.com/definitions/range-statistics-.html"""
    assert len(numbers) > 2, 'Length of Numbers is Greater than 2'
    assert isinstance(numbers, collections.Iterable), ' Is Iterable'
    numbers = sorted(numbers)
    range_2 = numbers[len(numbers) - 1] - numbers[0]
    return range_2

def standard_deviation(numbers):
    """Finds the standard deviation of a list of numbers, a measure of variance.
     See: https://www.mathsisfun.com/data/standard-deviation-formulas.html"""
    assert len(numbers) > 3, 'Length of Numbers Must Be More than 3'
    assert isinstance(numbers, collections.Iterable), 'Is Iterable'
    stdev = statistics.stdev(numbers)
    round_stdev = round(stdev, 2)
    return round_stdev
