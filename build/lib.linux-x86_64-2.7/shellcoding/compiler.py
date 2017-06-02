#!/usr/bin/env python3.6
import subprocess
import os
import sys
import time


class DependencyCheck(object):
    def __init__(self, command):
        self.command = command
        self.status = self._check()

    def _parse_which_resp(self, response):
        if os.path.exists(response):
            return True
        else:
            return False

    def _check(self):
        proc = subprocess.Popen("which {0} | awk {'print $1'}".format(self.command), \
                stdout=subprocess.PIPE, \
                stderr=subprocess.PIPE, \
                )
        stdout, stderr = proc.communicate()
        return self._parse_exists(stdout)


class Compiler(object):
    def __init__(self, asm_file, system_os, arch):
        self.asm_name = os.path.abspath(asm_file)
        self.base_name, ext = os.path.splitext(self.asm_name)
        self.arch = arch
        self.os = system_os
        self.deps = ["nasm", "ld"]
        self._compile()

    def _check_deps(self):
        deps_stats = [CheckDependency(x) for x in self.deps]
        missing_dependencies = filter(lambda x: x.status is False, deps_stats)
        for dependency in missing_dependencies:
            print("[!] Dependency is missing: {0}".format(dependency.command))

        if len(missing_dependencies) > 0:
            sys.exit(-1)
        return 0

    def _parse_args(self):
        """
        Parse the arch chosen by the user
        """
        parsed = dict()
        for dep in self.deps:
            parsed[dep] = ""

        if self.os == "posix":
            if self.arch == "x64":
                parsed["nasm"] = "elf64"
                parsed["ld"] = "elf_x86_64"
                return parsed
            elif self.arch == "x86":
                parsed["nasm"] = "elf32"
                parsed["ld"] = "elf32_x86_64"
                return parsed

        return 0

    def _link(self, parse):
        proc = subprocess.Popen("ld -m {0} -o {1} {2}.o".format(parse["ld"], self.base_name, self.base_name), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while proc.poll() is None:
            time.sleep(1)
        return proc.poll()

    def _compile(self):
        """
        Execute the steps necessary to compile asm code.
        """
        parse = self._parse_args()
        if not parse:
            print("[!] Error: options parsing.")
            return -1

        proc = subprocess.Popen("nasm -f {0} {1}".format(parse["nasm"], self.asm_name), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while proc.poll() is None:
            time.sleep(1)
        if proc.poll() == 0:
            print("[+] Assembly code successfullly assembled.")
            if self._link(parse) == 0:
                print("[+] Assembly object successfully linked.")
                return 0
            else:
                print("[!] Error: linking object.")
                return -1
        else:
            print("[!] Error: assembling code.")
            return proc.poll()


if __name__ == "__main__":
    main()
