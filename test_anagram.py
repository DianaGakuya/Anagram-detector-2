from anagram import Anagram

def test_anagram():
    listen = Anagram("listen")
    assert listen.match(['enlists', 'google', 'inlets', 'banana']) == ['inlets']
    assert listen.match(['enlists', 'google', 'banana']) == []
    assert listen.match(['enlists', 'google', 'silent']) == ['silent']
