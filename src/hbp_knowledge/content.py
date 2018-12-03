# -*- coding: utf-8 -*-

"""A python wrapper for accessing the knowledge curated in BEL during the Human Brain Pharmacome project."""

import os

from hbp_knowledge.constants import BEL_DIRECTORY


def list_content():
    """List the contents of the BEL directory."""
    for path in iterate_content():
        print(path)


def iterate_content():
    """Iterate over the absolute paths to files in the BEL directory."""
    for filename in os.listdir(BEL_DIRECTORY):
        yield os.path.join(BEL_DIRECTORY, filename)


if __name__ == '__main__':
    list_content()
