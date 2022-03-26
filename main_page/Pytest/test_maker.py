import pytest

""" Using Maker """

@pytest.mark.functional
def test_login():
    print("Executing login test",end=" ")

@pytest.mark.regression
def test_user_reg():
    print("Executing user reg test",end=" ")

@pytest.mark.functional
def test_compose_email():
    print("Executing compose email",end=" ")
