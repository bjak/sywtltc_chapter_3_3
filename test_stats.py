"""Test for Stats Function"""

import stats

def test_stats():
    """Tests for Stats"""
    assert stats.median([1, 2, 3, 4, 5]) == 3
    assert stats.median([5, 7, 9, 11, 13]) == 9
    assert stats.median([3, 6, 9, 12, 15]) == 9
