from closed_range.__init__ import version


def test_check_version():
    expected_version = "0.1.0"
    assert version == expected_version
