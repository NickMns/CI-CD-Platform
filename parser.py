import yaml

def load_yaml():
    with open(".cf.yaml", "r") as stream:
        try:
            content = yaml.safe_load(stream)
            print(content)
            return content
        except yaml.YAMLError as exc:
            print(exc)

def validate_yaml(content):
    # Validate contents of .cf.yaml file
    if "language" not in content:
        print("Error: language parameter not specified")

if __name__ == "__main__":
    # Load .cf.yaml (safe_load)
    conf_f = load_yaml()

    # Validate yaml for configuration errors
    validate_yaml(conf_f)
    
    # Prepare build scripts (depending on configuration provided)
    # builder.py