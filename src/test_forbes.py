def test_load_forbes():
    """Test forbes loading function."""
    from forbes import load_forbes, FORBES_FILE
    assert isinstance(load_forbes(FORBES_FILE), list)
