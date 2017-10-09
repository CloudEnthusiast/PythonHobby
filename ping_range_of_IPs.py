# ping test the range of IPs like 192.168.56.102 upto 192.168.56.105

import subprocess
import os
import platform

for n in range(102,105):
        ip="192.168.56.{0}".format(n)
        proc = subprocess.Popen( ['ping', '-c', '3', ip],stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        # Popen.communicate() interacts with process and return a tuple (stdoutdata, stderrdata)
        # It will Send data to stdin, Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate
        if proc.returncode == 0:
            print 'Active %s' %ip
        else:
            print '!! Inactive %s' %ip
