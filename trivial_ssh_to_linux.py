# This script will do ssh from 1 linux system to another linux
# and execute the provided COMMAND on another linux, gives its output

import subprocess
import sys

# Target server
HOST="192.168.56.102" 

# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
