# tests/test_reachability.py

from reachability import can_reach

def test_no_route():
    result, reason = can_reach(None, "10.0.0.1", {})
    assert result is False
