from py5_markup.element import Element

def test_context_manager():
    with Element() as e1:
        print("e1", e1)
        with Element() as e2:
            assert e1.get_parent() is None
            assert e2.get_parent() is e1
            assert e1.get_children() == [e2]
            assert e2.get_children() == []
        with Element() as e3:
            assert e1.get_children() == [e2,e3]
            assert e2.get_children() == []
            assert e3.get_children() == []
            with Element() as e5:
                with Element() as e6:
                    assert e5.get_parent() is e3
                    assert e5.get_children() == [e6]
                    assert e6.get_children() == []
    with Element() as e4:
        assert e1.get_children() == [e2,e3]
        assert e2.get_children() == []
        assert e3.get_children() == [e5]
        assert e4.get_children() == []
        assert e4.get_parent() is None

                