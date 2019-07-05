#!/usr/bin/env python
"""Expose EasyRSA features via a Python API"""

from easyrsa_wrapper import EasyRSA_Wrapper

import os.path
import csv


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

    def list_clients(self):
        client_certificate_index = []
        with open(self.easyrsa_directory + "/pki/index.txt") as indexfile:
            for line in csv.reader(indexfile, dialect="excel-tab"):
                if line[0]:
                    this_certificate = {}
                    this_certificate["status_flag"] = line[0]
                    this_certificate["expiration_date"] = line[1]
                    this_certificate["revocation_date"] = line[2]
                    this_certificate["serial_number"] = line[3]
                    this_certificate["filename"] = line[4]
                    this_certificate["certificate_cn"] = line[5]
                    client_certificate_index.append(this_certificate)
        return client_certificate_index