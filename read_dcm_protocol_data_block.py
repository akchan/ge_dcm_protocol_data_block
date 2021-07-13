#!/usr/bin/env python
# coding: UTF-8


import sys


import pydicom
import gzip


def read_dcm_protocol_data_block(dcm_path):
    dcm = pydicom.read_file(dcm_path)

    # Read a dicom element in bytes
    elm = dcm[0x0025,0x101b].value

    # Eliminate first 4 bytes and unzip
    protocol_data_block = gzip.decompress(elm[4:]).decode('ascii')

    return protocol_data_block


def main(dcm_path):
    str_protocol_data = read_dcm_protocol_data_block(dcm_path)
    print(str_protocol_data)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for dcm_path in sys.argv[1:]:
            main(dcm_path)
