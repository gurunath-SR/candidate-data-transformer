from normalizers.name_normalizer import normalize_name


def test_name():

    assert normalize_name("john smith") == "John Smith"


def test_name_spaces():

    assert normalize_name("  john    smith ") == "John Smith"