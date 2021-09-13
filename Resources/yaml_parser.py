import yaml, json


if __name__ == "__main__":
    with open('Resources/Data/inventory.yaml') as f:
        my_dict = yaml.safe_load(f)
        print(type(my_dict))
        print(json.dumps(my_dict, indent=4))
