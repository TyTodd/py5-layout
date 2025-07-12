from py5_markup.element import Element

def test_context_manager():
    with Element() as e1:
        print("e1", e1)
        with Element() as e2:
            assert e1.get_parent() is None
            assert e2.get_parent() is e1
            assert e1.get_children() == [e2]
            assert e2.get_children() == []