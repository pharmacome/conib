<h1 align="center">
  <br>
  HBP Knowledge
  <a href="https://travis-ci.com/pharmacome/knowledge">
    <img src="https://travis-ci.com/pharmacome/knowledge.svg?branch=master"
         alt="Travis CI">
  </a>
  <a href="https://zenodo.org/badge/latestdoi/159803376">
  	<img src="https://zenodo.org/badge/159803376.svg" alt="DOI">
  </a>
  <br>
</h1>

<p align="center">
This repository contains knowledge curated in Biological Expression Language (BEL)
for the Human Brain Pharmacome (HBP) project.
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

## Content

- [hbp_knowledge](https://github.com/pharmacome/knowledge/tree/master/hbp_knowledge): This folder contains curated BEL documents. Most have been organized by category (protein of interest, biological process of interest, pathway, etc.). AMost BEL documents correspond to a single publication, but a select few contain content from several due to topic-based curation.
- [docs](https://github.com/pharmacome/knowledge/tree/master/docs): This folder contains automatically generated HTML summaries of the content that can best be accesed through https://pharmacome.github.io/knowledge.
- [notebooks](https://github.com/pharmacome/knowledge/tree/master/notebooks): This folder contains various Jupyter notebooks associated with the repository. Since many of them use PyBEL-Jupyter, they may be best viewed using [NBViewer](https://nbviewer.jupyter.org/github/pharmacome/knowledge/tree/master/notebooks/).

## Installation
``hbp_knowledge`` can be installed from [PyPI](https://pypi.org/project/hbp-knowledge/) with the following command:

```bash
$ pip install hbp_knowledge
```

or the latest version can be installed from [GitHub](https://github.com/pharmacome/knowledge) with:

```bash
$ pip install git+https://github.com/pharmacome/knowledge.git
```

## Usage

The graph can be loaded with:

```python
from hbp_knowledge import get_graphs
from pybel import union

# Get all graphs
graphs = get_graphs()

# Combine them all using pybel.union
graph = union(graphs.values())
```

## Contributing

Contributions are welcome! Please submit all pull requests to https://github.com/pharmacome/knowledge.

## License

- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.
