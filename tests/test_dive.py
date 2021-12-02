from dive import get_submarine_position

def test_get_submarine_position():
    result = get_submarine_position('tests/test_dive_input.txt')
    assert result == 150