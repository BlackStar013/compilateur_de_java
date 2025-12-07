from nodes_class import *

def test_construir():
    r = Node('r')
    f = Node('f', r)
    f1 = Node('f1'); f2 = Node('f2',f)
    lf = [f1,f2]
    f1.set_parent(f)
    r.add_fils(f)
    f.add_list_fils(lf)

    assert(r.fils == [f])
    assert(f.parent == r)
    assert(f.fils == lf)
    assert(f1.parent == f)
   
