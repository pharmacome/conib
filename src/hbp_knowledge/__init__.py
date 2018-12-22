# -*- coding: utf-8 -*-

"""The Human Brain Pharmacome knowledge repository."""

import os

from bel_repository import BELRepository

__all__ = [
    'HERE',
    'BEL_DIRECTORY',
    'repository',
    'get_graph',
    'get_graphs',
    'get_summary_df',
]

HERE = os.path.abspath(os.path.dirname(__file__))
BEL_DIRECTORY = os.path.abspath(os.path.join(HERE, os.path.pardir, os.path.pardir, 'bel'))

repository = BELRepository(BEL_DIRECTORY)
get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df
