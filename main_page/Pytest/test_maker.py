import pytest

""" Using Maker  and parametrize """

@pytest.mark.functional
def test_login():
    print("Executing login test",end=" ")

@pytest.mark.regression
def test_user_reg():
    print("Executing user reg test",end=" ")

@pytest.mark.functional
def test_compose_email():
    print("Executing compose email",end=" ")


def get_data():
    return [
        ("balaji","jljlj"),
        ("walke","kjkjkj")
    ]


@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    print(username,"----",password)





