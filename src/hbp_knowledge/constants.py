# -*- coding: utf-8 -*-

"""Constants for the Human Brain Pharmacome knowledge repository."""

import os

__all__ = [
    'VERSION',
    'HERE',
    'BEL_DIRECTORY',
]

VERSION = '0.0.1-dev'
HERE = os.path.abspath(os.path.dirname(__file__))
BEL_DIRECTORY = os.path.abspath(os.path.join(HERE, os.path.pardir, os.path.pardir, 'bel'))
