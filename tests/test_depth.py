from depths import get_depth_changes

def test_get_depth_changes():
    result = get_depth_changes('tests/test_depths_input.txt')
    assert result == 5