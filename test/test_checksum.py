from src.checksum import modulo_11_checksum


def test_good():
    assert modulo_11_checksum("2-266-11156-8")


def test_bad():
    assert not modulo_11_checksum("2-266-11156-3")
