# -*- coding: utf-8 -*-

"""The Curation of Neurodegeneration in BEL (CONIB) repository."""

import os

from pybel.repository import BELMetadata, BELRepository

__all__ = [
    'repository',
    'metadata',
    'get_graph',
    'get_graphs',
    'get_indra_statements',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.8'

# Author list will be sorted by last name
AUTHORS = [
    'Charles Tapley Hoyt',
    'Daniel Domingo-Fernández',
    'Esther Wollert',
    'Sandra Spalek',
    'Rana Al Disi',
    'Lingling Xu',
    'Kristian Kolpeja',
    'Yojana Gadiya',
    'Trusha Adeshara',
    'Stephan Gebel',
    'Sepehr Golriz',
]

description = "Mechanistic knowledge surrounding several neurodegenerative diseases," \
              " with specific focus on protein aggregation, nicotinic receptor signalling," \
              " proteostasis, and other mechanisms."

# All metadata is grouped here
metadata = BELMetadata(
    name='Curation of Neurodegeneration in BEL (CONIB)',
    version=VERSION,
    authors=', '.join(AUTHORS),
    contact='cthoyt@gmail.com',
    description=description,
    license='CC0 1.0 Universal',
    copyright='Copyright © 2019 Fraunhofer SCAI, All rights reserved.',
)

repository = BELRepository(
    HERE,
    metadata=metadata,
)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_indra_statements = repository.get_indra_statements
get_summary_df = repository.get_summary_df

main = repository.build_cli()
