import pytest, yaml
from Resources.yaml_parser import yaml_parser

@pytest.fixture(scope="function")
def triplify(request):
    return request.param * 3


@pytest.fixture(scope="function")
def double(request):
    return request.param * 2

@pytest.fixture(scope="function")
def yaml_eater(request) -> list:
    """Fixture version of the yaml parser from Resources/yaml_parser.py for experimentation purposes."""
    target_dir: str = 'Resources/Data/inventory.yaml'
    with open(target_dir) as f:
        my_dict = yaml.safe_load(f)
        return my_dict.get(request.param)

@pytest.mark.parametrize("triplify, double", [("a", "b")], indirect=["triplify", "double"])
def test_indirect(triplify, double):
    """Example of using indirect parameterization. First part of the parametrize argument is the name of the fixture that we're going to use, second part in a list is the list of parametres we're passing to the fixture as parameters, and lastly the source of indirect parameters which in this case is still the name of the fixtures. Otherwise I would use indirect=True."""
    assert triplify == "aaa"
    assert double == "bb"

# @pytest.mark.skip()
@pytest.mark.parametrize("value", yaml_parser('Name (Z to A)'))
def test_get_yaml_info_individually(value):
    """Pulls individual items from that yaml file's values where the required argument is the key value in the yaml file. Checks if value is part of the given list and if value is a string."""
    print(value)
    assert value in ["Sauce Labs Onesie", "Sauce Labs Bike Light",
                     "Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)", "Sauce Labs Fleece Jacket"]
    assert isinstance(value, str)


@pytest.mark.parametrize("yaml_eater", ["Name (Z to A)", "Price (low to high)"], indirect=True)
def test_get_yaml_info_as_a_list(yaml_eater):
    """Prints information from yaml file from a given key as the argument. Using indirect parameterization to utilize potentially multiple paramters."""
    print(yaml_eater)
    assert isinstance(yaml_eater, list)


"""
    indirect parametrization : 
        :: Using indirect parametrization : https://stackoverflow.com/questions/18011902/pass-a-parameter-to-a-fixture-function

        :: official documentation: https://docs.pytest.org/en/latest/example/parametrize.html#indirect-parametrization

    parametrizing tests via functions:
        :: stackoverflow article : https://stackoverflow.com/questions/51950921/parameterize-tests-using-excel-in-pytest

        :: 

"""
