"""Some simple statistical functions."""

import collections
import numbers

def mean(number_list):
    """Takes the mean/average of a list of numbers, a simple measure of 'middle'. See: https://en.wikipedia.org/wiki/Arithmetic_mean"""
    #preconditions, assumptions
    assert isinstance(numbers, collections.Iterable), "Must be list or list like"
    assert len(data) > 0, "Mean of empty list is undefined"
    assert isinstance(numbers[0], numbers.Number), "Only works on numbers"

    mean_ = 0.0

    #postconditions, promises
    assert isinstance(mean_, numbers.Number), "Mean will be a number"
    assert mean_ >= min(number_list), "The mean needs to be greater than or equal to the smallest number in number_list"
    assert mean_ <= max(number_list), "The mean needs to be smaller than or equal to the smallest number in number_list"

def median(number_list):
    """Finds the median or middle of a list of sorted numbers, a simple measure of 'middle'. See: https://en.wikipedia.org/wiki/Median"""
    #preconditions, assumptions
    assert isinstance(numbers, collections.Iterable), "Must be list or list like"
    assert len(data) > 0, "Median of empty list is undefined"
    assert isinstance(numbers[0], numbers.Number), "Only works on numbers"
    assert sorted(number_list) == number_list, "List needs to be sorted"

    median_ = 0.0

    #postconditions, promises
    assert isinstance(median_, numbers.Number), "Mean will be a number"
    assert median_ >= min(number_list), "The mean needs to be greater than or equal to the smallest number in number_list"
    assert median_ <= max(number_list), "The mean needs to be smaller than or equal to the smallest number in number_list"

def statistical_range(number_list):
    """Finds ths range of a list of numbers, a simple measure of variance. See: https://www.mathsisfun.com/definitions/range-statistics-.html"""
    #preconditions, assumptions
    assert isinstance(numbers, collections.Iterable), "Must be list or list like"
    assert len(data) > 1, "Range of empty or 1 length list is undefined"
    assert isinstance(numbers[0], numbers.Number), "Only works on numbers"

    statistical_range_ = 0.0

    #postconditions, promises
    assert isinstance(statistical_range_, numbers.Number), "Mean will be a number"
    assert max(number_list) - statistical_range_ == min(number_list), "Max and min of number_list should be excatly statistical_range_ apart"

def standard_deviation(number_list):
    """Finds the standard deviation of a list of numbers, a measure of variance. See: https://www.mathsisfun.com/data/standard-deviation-formulas.html"""
    #preconditions, assumptions
    assert isinstance(numbers, collections.Iterable), "Must be list or list like"
    assert len(data) > 0, "Mean of empty list is undefined"
    assert isinstance(numbers[0], numbers.Number), "Only works on numbers"

    standard_deviation_ = 0.0

    #postconditions, promises
    assert isinstance(statistical_range_, numbers.Number), "Mean will be a number"
    assert standard_deviation_ <= range(number_list), "The standard deviation should always be less than or equal to the range."
