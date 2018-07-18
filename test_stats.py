"""Test for Stats Function"""

import stats

def test_stats_median():
    """Tests for Median Function Stats"""
    assert stats.median([1, 2, 3, 4, 5]) == 3
    assert stats.median([5, 7, 9, 11, 13]) == 9
    assert stats.median([3, 6, 9, 12, 15]) == 9

def test_stats_range_1():
    """Tests for Range Function Stats"""
    assert stats.range_1([1, 2, 3, 4, 5]) == 4
    assert stats.range_1([5, 10, 15, 20, 25]) == 20
    assert stats.range_1([4, 2, 10, 8, 6, 3, 5, 7, 9, 1]) == 9

def test_stats_mean():
    """Test for Mean Function Stats"""
    assert stats.mean([1, 2, 3, 4, 5]) == 3
    assert stats.mean([3, 6, 9, 12, 15, 18, 21]) == 12
    assert stats.mean([5, 10, 15, 20, 25, 30]) == 17.5

def test_stats_stdev():
    """Test for Standard Deviation"""
    assert stats.standard_deviation([2, 4, 6, 8, 10]) == 3.16
    assert stats.standard_deviation([1, 2, 3, 4, 5]) == 1.58
    assert stats.standard_deviation([5, 10, 15, 20, 25]) == 7.91
