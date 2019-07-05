#!/usr/bin/env python
"""Interact with the EasyRSA v3 executable"""

import os.path
import subprocess

class EasyRSA_Wrapper(object):
    """
    Class to handle interactions with the EasyRSA executable

    Should only be called by easypysa.py, all of the sanity checks and validation are done
    in the user facing module.
    """
    def __init__(self, easyrsa_directory):
        """
        Returns an EasyRSA_Wrapper empty object
        """
        self.easyrsa_directory = easyrsa_directory
        self.easyrsa_executable = easyrsa_directory + "/easyrsa"

    def check_executable(self):
        try:
            check_ca = subprocess.check_call([self.easyrsa_executable, "check_ca"])
            return "OK"
        except subprocess.CalledProcessError as error:
            print error
            raise