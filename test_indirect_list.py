import pytest


@pytest.fixture(scope="function")
def triplify(request):
    return request.param * 3


@pytest.fixture(scope="function")
def double(request):
    return request.param * 2


@pytest.mark.parametrize("triplify, double", [("a", "b")], indirect=["triplify", "double"])
def test_indirect(triplify, double):
    assert triplify == "aaa"
    assert double == "bb"

"""
    

"""