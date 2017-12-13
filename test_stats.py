"""Test for Stats Function"""

import stats

def test_stats_median():
    """Tests for Median Function Stats"""
    assert stats.median([1, 2, 3, 4, 5]) == 3
    assert stats.median([5, 7, 9, 11, 13]) == 9
    assert stats.median([3, 6, 9, 12, 15]) == 9

def test_stats_range():
    """Tests for Range Function Stats"""
    assert stats.range([1, 2, 3, 4, 5]) == 4
    assert stats.range([5, 10, 15, 20, 25]) == 20
    assert stats.range([2, 4, 6, 8, 10]) == 8
