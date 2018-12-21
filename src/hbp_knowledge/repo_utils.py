# -*- coding: utf-8 -*-

"""Utilities for BEL repositories."""

import logging
import os
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Optional, Tuple, Union

import pandas as pd
from tqdm import tqdm

from pybel import BELGraph, Manager, from_path, from_pickle, to_pickle, union

__all__ = [
    'BELRepository',
]

logger = logging.getLogger(__name__)


@dataclass
class BELRepository:
    """A container for a BEL repository."""

    input_directory: str
    output_directory: Optional[str] = None
    bel_pickle_name: str = 'union.bel.pickle'
    bel_summary_name: str = 'union_summary.tsv'

    @property
    def _cache_directory(self):
        return self.output_directory or self.input_directory

    @property
    def bel_pickle_path(self):
        return os.path.join(self._cache_directory, self.bel_pickle_name)

    @property
    def bel_summary_path(self):
        return os.path.join(self._cache_directory, self.bel_summary_name)

    def walk(self):
        """Recursively walk this directory."""
        return os.walk(self.input_directory)

    def iterate_bel(self) -> Iterable[Tuple[str, str]]:
        """Yield all paths to BEL documents."""
        for root, dirs, files in self.walk():
            for file in files:
                if file.endswith('.bel'):
                    yield root, file

    def _build_cache_path(self, root, file):
        return os.path.join((self.output_directory if self.output_directory else root), f'{file}.pickle')

    @property
    def _global_cache_exists(self) -> bool:
        """Return if this repository already been cached as a single file."""
        return os.path.exists(self.bel_pickle_path)

    def _load_global_cache(self) -> BELGraph:
        """Return the global cache."""
        return from_pickle(self.bel_pickle_path)

    def get_graph(self,
                  manager: Optional[Manager] = None,
                  use_cached: bool = False,
                  use_tqdm: bool = False,
                  tqdm_kwargs: Optional[Mapping[str, Any]] = None,
                  from_path_kwargs: Optional[Mapping[str, Any]] = None,
                  ) -> BELGraph:
        if use_cached and self._global_cache_exists:
            return self._load_global_cache()

        graphs = self.get_graphs(
            manager=manager,
            use_tqdm=use_tqdm,
            tqdm_kwargs=tqdm_kwargs,
            from_path_kwargs=from_path_kwargs,
        )
        graph = union(graphs.values())
        to_pickle(graph, self.bel_pickle_path)
        return graph

    def get_graphs(self,
                   manager: Optional[Manager] = None,
                   use_cached: bool = False,
                   use_tqdm: bool = False,
                   tqdm_kwargs: Optional[Mapping[str, Any]] = None,
                   from_path_kwargs: Optional[Mapping[str, Any]] = None,
                   ) -> Mapping[str, BELGraph]:
        if manager is None:
            manager = Manager()

        paths = self.iterate_bel()
        if use_tqdm:
            paths = tqdm(list(paths), **(tqdm_kwargs or {}))

        rv = {}
        for root, file in paths:
            path = os.path.join(root, file)
            pickle_path = self._build_cache_path(root, path)

            if os.path.exists(pickle_path) and use_cached:
                rv[path] = from_pickle(pickle_path)
                continue

            graph = rv[path] = from_path(path, manager=manager, **(from_path_kwargs or {}))

            if graph.warnings:
                logger.info(f' - {len(graph.warnings)} warnings')

            to_pickle(graph, pickle_path)

        return rv

    def get_summary_df(self,
                       manager: Optional[Manager] = None,
                       use_cached: bool = False,
                       use_tqdm: bool = False,
                       tqdm_kwargs: Optional[Mapping[str, Any]] = None,
                       from_path_kwargs: Optional[Mapping[str, Any]] = None,
                       save: Union[bool, str] = True
                       ) -> pd.DataFrame:
        graphs = self.get_graphs(
            manager=manager,
            use_cached=use_cached,
            use_tqdm=use_tqdm,
            tqdm_kwargs=tqdm_kwargs,
            from_path_kwargs=from_path_kwargs,
        )

        df = pd.DataFrame.from_dict(
            {
                path: dict(
                    title=graph.name,
                    author=graph.authors,
                    **graph.summary_dict(),
                )
                for path, graph in graphs.items()
            },
            orient='index',
        )

        if isinstance(save, str):
            df.to_csv(save, sep='\t')
        elif save:
            df.to_csv(self.bel_summary_path, sep='\t')

        return df
