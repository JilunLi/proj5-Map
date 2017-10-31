from poi import Poi

def test_getList():
    file  = 'data/poi.dat'
    assert Poi(file)
    assert isinstance(Poi(file).getList(), list)
