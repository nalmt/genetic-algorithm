# coding : utf8
# !/usr/bin/env python

import subprocess

STUDENT_ID = 11806768

def check(student_id , passwords) :
    proc = subprocess.Popen(["./unlock", str(student_id)] + passwords, stdout = subprocess.PIPE)
    results = []
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        results.append(float(str(line).split("\\t")[1].split("\\n")[0]))
    return results

print(check(STUDENT_ID, ["PASSWORD", "ALGOGEN"]))