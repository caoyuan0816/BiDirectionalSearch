"""
ASU CSE571 Artificial Intelligence Team Project.
--------------------------------------------------------------------------------
test.py
--------------------------------------------------------------------------------
****
IMPORTANT: That script can only run for python3.3+
Other files in that project need python2.

It's not part of project and only used to generate test result faster.
****
"""
import os
import sys
import subprocess

# Set running path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)

if __name__ == '__main__':
    try:
        os.remove(ROOT_PATH + '/out.txt')
    except OSError:
        pass

    algorithm = sys.argv[1]
    for i in range(1, 12):
        command = ['python2', 'rubikCube.py', 'multi', 'multi_rand_'+str(i), algorithm]

        try:
            res = subprocess.check_output(command, timeout=int(sys.argv[2])).decode("utf-8")
            avg = res.split('\n')[-2]
        except subprocess.TimeoutExpired:
            break

        with open(ROOT_PATH + '/' + 'out.txt', 'a') as output:
            output.write(avg+'\n')
