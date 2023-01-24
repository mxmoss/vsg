import os
import platform
import subprocess
import tempfile

def isWindows():
    return (platform.system() == 'Windows')

def tmpFileName(seed = None):
    if isWindows():
        suffix = '.bat'
    else:
        suffix = '.sh'
    if seed:
        suffix = '-' + seed + suffix
    return tempfile.TemporaryFile(suffix = suffix, prefix = 'AWSInstance')

def exec(command, params):
    #    os.path.abspath(os.path.dirname(__file__))
    # Create list with arguments for subprocess.call
    args = []
    args.append(command)
    for i in params.split():
        args.append(i)
    # Run subprocess.run and save output object
    output = subprocess.run(args, capture_output=True)
    print('Return code:', output.returncode)
    # use decode function to convert to string
    print('Output:', output.stdout.decode("utf-8"))
    return output
