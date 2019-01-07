# -*- coding: utf-8 -*-

"""The Human Brain Pharmacome knowledge repository."""

import os

from bel_repository import BELMetadata, BELRepository
from bel_repository.utils import serialize_authors

__all__ = [
    'repository',
    'metadata',
    'get_graph',
    'get_graphs',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

# Author list will be sorted by last name
AUTHORS = [
    'Charles Tapley Hoyt',
    'Daniel Domingo-Fernández',
    'Esther Wollert',
    'Sandra Spalek',
    'Rana Al Disi',
    'Lingling Xu',
    'Kristian Kolpeja',
]

# All metadata is grouped here
metadata = BELMetadata(
    name='Human Brain Pharmacome Knowledge',
    version=VERSION,
    authors=serialize_authors(AUTHORS),
    contact='charles.hoyt@scai.fraunhofer.de',
)

repository = BELRepository(
    HERE,
    bel_metadata=metadata,
)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df

main = repository.build_cli()
