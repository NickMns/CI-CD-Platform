import os
import yaml
import logging
import logging.config

import parse_exceptions as pex

DUMMY_PROJECT_DIR = "\Projects\Dummy"

def load_yaml():
    with open(".cf.yaml", "r") as stream:
        try:
            content = yaml.safe_load(stream)
            #print(content)
            return content
        except yaml.YAMLError as exc:
            #print(exc)
            logging.exception(exc)

'''
.cf.yaml validation rules
'''
def validate_yaml(content):
    if "language" not in content:
        pass
        #raise pex.LanguageNotDefined
    if "before_script" in content:
        stepsBefore = content["before_script"]
        logging.info("Before Script = {}".format(stepsBefore))

def main():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.config.fileConfig("logging.conf")

    conf_f = load_yaml()

    # Validate yaml for configuration errors
    validate_yaml(conf_f)

    from builder import run_shell_command
    from builder import run_shell_script

    run_shell_command("ls -a")
    #run_shell_command("cd build_scripts/")
    run_shell_command("ls -al")
    #logging.info("Current Working Directory = {}".format(os.getcwd()))

    script_path = os.path.join(os.getcwd(), "build_scripts/test.sh")
    run_shell_script([script_path])

    # Prepare build scripts (depending on configuration provided)
    # builder.py

if __name__ == "__main__":
    main()

    
