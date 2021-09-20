import yaml


def yaml_parser(
        target_values: str, 
        target_dir: str = 'Resources/Data/inventory.yaml') -> list:
    """Using a string, gets the directory where yaml file is stored and parses information inside it. Returns a list of the target values from the yaml file."""
    with open(target_dir) as f:
        my_dict = yaml.safe_load(f)
        return my_dict.get(target_values)

# added this to test out the function above
if __name__ == "__main__":
    # to run this must comment out line that makes function a fixture - otherwise
    # will get Failed: Fixture "yaml_parser" called directly. Fixtures are not meant to be called directly,
    print(yaml_parser('Name (Z to A)'))
