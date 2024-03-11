#!/usr/bin/env python3

import subprocess
import sys
import os
import shutil

from snakemake.utils import read_job_properties

jobscript = sys.argv[1]
job_properties = read_job_properties(jobscript)


# Submit the job