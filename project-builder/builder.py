# Takes as input the contents of '.cf.yaml' file 
# Generates the respective build scripts that will be used during code integration (CI)
import os
import subprocess

def call_bash_command(command):
    print("start -- call command {}".format(command[:5]))
    subprocess.call(command,shell=True)
    print("end -- call command {}".format(command[:5])) 

def call_script(script_name):
    print("start -- call script {}".format(script_name))
    subprocess.call(script_name,shell=True) # cwd=os.path.join(os.getcwd(), "build_scripts"
    print("end -- call script {}".format(script_name))
