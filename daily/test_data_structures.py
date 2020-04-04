from .data_structures import *


def test_product_of_all_other_items():
    given = [1, 2, 3, 4, 5]
    expect = [120, 60, 40, 30, 24]

    result = product_of_all_other_items(given)
    assert result == expect
