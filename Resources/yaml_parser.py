import yaml, json

def yaml_parser(target_dir: str, target_values: str) -> list:
    """Using a string, gets the directory where yaml file is stored and parses information inside it."""
    with open(target_dir) as f:
        my_dict = yaml.safe_load(f)
        return my_dict.get(target_values)


if __name__ == "__main__":
    the_d = yaml_parser(
        target_dir="Resources/Data/inventory.yaml",
        target_values="Price (high to low)"
        )
    print(the_d)