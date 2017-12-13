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
    assert stats.range([4, 2, 10, 8, 6, 3, 5, 7, 9, 1]) == 9

def test_stats_mean():
    """Test for Mean Function Stats"""
    assert stats.mean([1, 2, 3, 4, 5]) == 3
    assert stats.mean([3, 6, 9, 12, 15, 18, 21]) == 12
    assert stats.mean([5, 10, 15, 20, 25, 30]) == 17.5
