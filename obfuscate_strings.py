#!/usr/bin/python

import argparse
import subprocess

parser = argparse.ArgumentParser(description='Obfuscate a whole string, including whitespaces.')
parser.add_argument('STRING')
args = parser.parse_args()

words = []
for word in args.STRING.split():
    process = subprocess.Popen(["./obfuscate_string.sh", word],
                               stdout=subprocess.PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    words.append(output.replace('\n', ''))
print " + \" \" + ".join(words)
