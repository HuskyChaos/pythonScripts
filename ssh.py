#!/bin/python3
import subprocess

subprocess.run(["sudo", "su"])

sub = subprocess.run(["sudo","service", "ssh", "status"], capture_output=True)
sub = sub.stdout.decode()

if "dead" in sub:
    subprocess.run(["sudo","systemctl","enable", "--now", "ssh"])

else:
    print("SSH Active")

rootlist = subprocess.run(["ls", "-la","/root/"], capture_output=True)
rootlist = rootlist.stdout.decode()
if ".ssh" not in rootlist:
    subprocess.run(["", ""])