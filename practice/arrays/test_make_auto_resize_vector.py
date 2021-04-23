import make_auto_resize_vector


def test_initial_size_is_0():
    v = make_auto_resize_vector.MyVector()
    assert v.size() == 0


def test_push_item_increases_size():
    v = make_auto_resize_vector.MyVector()
    v.push(123)
    assert v.size() == 1