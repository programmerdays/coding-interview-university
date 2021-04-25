import make_auto_resize_vector


def test_initial_size_is_0():
    v = make_auto_resize_vector.MyVector()
    assert v.size() == 0


def test_push_item_increases_size():
    v = make_auto_resize_vector.MyVector()
    v.push(123)
    assert v.size() == 1


def test_get_item():
    v = make_auto_resize_vector.MyVector()
    v.push(123)
    assert v[0] == 123


def test_push_push_pop_gets_correct_values():
    v = make_auto_resize_vector.MyVector()
    v.push(123)
    v.push(456)
    last_item = v.pop()
    assert last_item == 456
    last_item = v.pop()
    assert last_item == 123
