from py5_layout.element import Element
from py5_layout.py5_layout import Py5Layout

def test_context_manager():
    with Py5Layout() as layout: 
        with Element() as e1:
            with Element() as e2:
                assert e1.get_parent() is not None
                assert e1.get_parent()[1] == 0
                assert e2.get_parent()[0] is e1
                assert e2.get_parent()[1] == 0
                assert e1.get_children() == [e2]
                assert e2.get_children() == []
            with Element() as e3:
                assert e1.get_children() == [e2,e3]
                assert e2.get_children() == []
                assert e3.get_children() == []
                assert e3.get_parent()[1] == 1
                with Element() as e5:
                    with Element() as e6:
                        assert e5.get_parent()[0] is e3
                        assert e5.get_children() == [e6]
                        assert e6.get_children() == []
        with Element() as e4:
            assert e1.get_children() == [e2,e3]
            assert e2.get_children() == []
            assert e3.get_children() == [e5]
            assert e4.get_children() == []
            assert e4.get_parent() is not None
            assert e4.get_parent()[1] == 1

                