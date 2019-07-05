#!/usr/bin/env python
"""Expose EasyRSA features via a Python API"""

from easyrsa_wrapper import EasyRSA_Wrapper

import os.path


class EasyPysa(object):
    """
    Offers a number of functions to help OpenVPN administrators
    manage their client certificates
    """
    def __init__(self, easyrsa_directory="/etc/openvpn/ca"):
        """
        Returns an EasyRSA_Wrapper empty object

        :param easyrsa_directory: (str) path to a directory containing an easyrsa v3 install (defaults to /etc/openvpn/ca)
        """
        if os.path.isdir(easyrsa_directory):
            self.easyrsa_directory = easyrsa_directory
        else:
            raise ValueError("easyrsa_directory is not a directory")

        if not os.path.isfile(easyrsa_directory + ("/easyrsa")):
            raise ValueError("easyrsa_directory doesn't contain easyrsa script file")

        return

    def _check_executable(self):
        easy = EasyRSA_Wrapper(easyrsa_directory=self.easyrsa_directory)
        return easy.check_executable()
