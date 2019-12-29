import os
import yaml

DUMMY_PROJECT_DIR = "\Projects\Dummy"

def load_yaml():
    with open(".cf.yaml", "r") as stream:
        try:
            content = yaml.safe_load(stream)
            print(content)
            return content
        except yaml.YAMLError as exc:
            print(exc)

'''
.cf.yaml validation rules
'''
def validate_yaml(content):
    # Validate contents of .cf.yaml file
    if "language" not in content:
        print("Error: language parameter not specified")
    if "before_script" in content:
        stepsBefore = content["before_script"]
        print(stepsBefore)

if __name__ == "__main__":
    # Load .cf.yaml (safe_load)
    conf_f = load_yaml()

    # Validate yaml for configuration errors
    validate_yaml(conf_f)
    
    from builder import call_script
    from builder import call_bash_command

    call_bash_command("ls")
    call_bash_command("cd build_scripts")
    call_bash_command("ls")
    print(os.getcwd())
    script_path = os.path.join(os.getcwd(), "build_scripts/test.sh")
    print(script_path)
    call_script([script_path])
    # Prepare build scripts (depending on configuration provided)
    # builder.py

    
