import pytest
from Checkout import Checkout


# def test_CanInstantiateCheckout():
#     co = Checkout()

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 1)
    checkout.addItemPrice('b', 2)
    return checkout


# def test_CanAddItemPrice(checkout):
#     checkout.addItemPrice('a', 1)


# def test_CanAddItem(checkout):
#     checkout.addItem('a')


def test_CanCalculateTotal(checkout):
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1


def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3


def test_CanAddDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)


# @pytest.mark.skip()
def test_CanApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2


def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')