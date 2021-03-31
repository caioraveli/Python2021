import sys
import subprocess

HOST ='192.168.124.60'
command = 'ls -l'


com = subprocess.run(
    ['ping','192.168.124.60','-c','4']
)

con = subprocess.run(
    ['ssh','f13@192.168.124.60','ls']
    )