# -*- coding: utf-8 -*-

"""The Human Brain Pharmacome knowledge repository."""

import os

from bel_repository import BELRepository

__all__ = [
    'repository',
    'get_graph',
    'get_graphs',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

repository = BELRepository(HERE)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df

main = repository.build_cli()
