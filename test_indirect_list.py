import pytest
from Resources.yaml_parser import yaml_parser

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

@pytest.mark.parametrize("value", yaml_parser('Name (Z to A)'))
def test_get_yaml_info(value):
    print(value)


"""
    indirect parametrization : 
        :: Using indirect parametrization : https://stackoverflow.com/questions/18011902/pass-a-parameter-to-a-fixture-function

        :: official documentation: https://docs.pytest.org/en/latest/example/parametrize.html#indirect-parametrization

    parametrizing tests via functions:
        :: stackoverflow article : https://stackoverflow.com/questions/51950921/parameterize-tests-using-excel-in-pytest

        :: 

"""
