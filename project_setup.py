#!/usr/bin/env python3.6
import sys


#  Default file with project data
default_file = "project.data"

#  setup.py data
setup_data = """from setuptools import setup

setup(name='%s',
    version='%s',
    description='%s',
    url='%s',
    author='%s',
    author_email='%s',
    license='%s',
    packages=['%s'],
    package_dir={'%s': 'src'},
    package_data={'%s': ['src/*']},
    scripts=%s,
    zip_safe=False)
"""

def parse_data(f):
    data = dict()

    #  Open the file and get the uncommented data
    with open(f, "r") as f:
        for line in f.readlines():
            if line[0] is "#" or len(line) < 2:  # Ignore comments
                continue
            key, value = line.split("=")
            data[key] = str(value.replace("\n", "")).replace('"', "'")
    return data


def validate_data(data):
    REQUIRED_OPTIONS = [
            "PROJECT_NAME",
            "PROJECT_VERSION",
            "PROJECT_AUTHOR",
            ]

    for k in data:
        v = data[k]

        #  Check for empty data of required fields.
        if v is "" and k in REQUIRED_OPTIONS:
            print("[*] Validation error: {0} is empty.".format(k))
            sys.exit(-1)
        elif v is "":
            print("[+] Setting value of key '{0}' to 'None'".format(k))
            data[k] = "None"

    return data


def main():
    p = validate_data(parse_data(default_file))
    print(setup_data % (
        p["PROJECT_NAME"],
        p["PROJECT_VERSION"],
        p["PROJECT_DESCRIPTION"],
        p["PROJECT_URL"],
        p["PROJECT_AUTHOR"],
        p["AUTHOR_EMAIL"],
        p["PROJECT_LICENSE"],
        p["PROJECT_PACKAGE"],
        p["PROJECT_PACKAGE"],
        p["PROJECT_PACKAGE"],
        p["PROJECT_BINARIES"],
        ))
    return 0

if __name__ == "__main__":
    main()
