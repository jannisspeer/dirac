#!/usr/bin/env python

import subprocess
import sys

jobid = sys.argv[1]

class MissingJobError(Exception):
    pass

# try to get status
try:
    cmd = "dirac-wms-job-status {}".format(jobid)
    res = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    res = res.stdout.decode()
    if res == "":
        raise MissingJobError
    else:
        print(res.split(";")[2].removeprefix(" "))
except subprocess.CalledProcessError as e:
    print("Failed to get job status")
    if "No proxy found" in e.stdout.decode():
        print("DIRAC proxy expired. Please create a new proxy.")
    else:
        print("dirac-wms-job-status error: ", e.stdout, file=sys.stderr)
except MissingJobError as e:
    print("No output from dirac-wms-job-status. Job may not exist.")
