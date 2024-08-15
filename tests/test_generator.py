import pytest

from asdf23.generator import generate_randome_number


def test_generate_random_number_generates_random_numberj():
    assert generate_randome_number() in range(100)


def test_generate_random_number_generates_random_number():
    assert generate_randome_number() in range(100)


if __name__ == "__main__":
    pytest.main(["-s", "-v", __file__])
