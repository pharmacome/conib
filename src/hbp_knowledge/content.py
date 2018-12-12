# -*- coding: utf-8 -*-

"""A python wrapper for accessing the knowledge curated in BEL during the Human Brain Pharmacome project."""

import os
from typing import Mapping

from pybel import BELGraph

from hbp_knowledge.constants import BEL_DIRECTORY

__all__ = [
    'list_bel_paths',
    'iterate_bel_paths',
    'get_graphs',
]


def list_bel_paths():
    """List the contents of the BEL directory."""
    for path in iterate_bel_paths():
        print(path)


def iterate_bel_paths():
    """Iterate over the absolute paths to files in the BEL directory."""
    for filename in os.listdir(BEL_DIRECTORY):
        yield os.path.join(BEL_DIRECTORY, filename)


def get_graphs() -> Mapping[str, BELGraph]:
    """Get a dictionary of BEL graphs."""
    raise NotImplementedError


if __name__ == '__main__':
    list_bel_paths()
