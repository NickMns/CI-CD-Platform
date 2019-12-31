# Takes as input the contents of '.cf.yaml' file 
# Generates the respective build scripts that will be used during code integration (CI)
import subprocess
import logging
import logging.config
import shlex
import os
import io

logging.config.fileConfig("logging.conf")

def run_shell_command(command_line):
    command_line_args = shlex.split(command_line)
    logging.info('Subprocess: "' + command_line + '"')

    try:
        command_line_process = subprocess.Popen(
            command_line_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        process_output, _ =  command_line_process.communicate()

        buff = process_output.decode("utf-8")
        logging.debug("Subprocess output: {}".format(buff))
    except (OSError, subprocess.CalledProcessError) as exception:
        logging.debug('Exception occured: {}'.format(str(exception)))
        logging.debug('Subprocess failed')
        return False
    else:
        # no exception was raised
        logging.debug('Subprocess finished')

    return True

def run_shell_script(script_path):
    logging.info("Subprocess: {}".format(script_path))
    
    try:
        bash_script_process = subprocess.Popen(
            script_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        process_output, _ = bash_script_process.communicate()

        buff = process_output.decode("utf-8")
        logging.debug("Subprocess output: \n{}".format(buff))
    except (OSError, subprocess.CalledProcessError) as exception:
        logging.debug('Exception occured: {}'.format(str(exception)))
        logging.debug('Subprocess failed')
        return False
    else:
        # no exception was raised
        logging.debug('Subprocess finished')

    return True