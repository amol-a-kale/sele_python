import pytest
from pytestfunctions import arithmetic_module  # import file from pytestfuntions package

# AAA
# A-arrange
# A-action
# A-assertion/validation

# if we want to give ordering to test case for that we have to use one of the py test feature ordering
# install (pip install pytest-ordering ) package before run program

@pytest.mark.run(order=1)  # this is syntax for ordering test cases and pytest is one of the decorator
def test_add():
    res = arithmetic_module.add(20, 30)
    assert res == 50
    res = arithmetic_module.add(20.30, 20.70)
    assert res == 40  # assert used for compare true or false or validation of statement


@pytest.mark.run(order=3)
def test_mod():
    res = arithmetic_module.mod(20, 10)
    assert res == 0


@pytest.mark.run(order=2)
def test_mul():
    res = arithmetic_module.product(20, 30)
    assert res == 600

