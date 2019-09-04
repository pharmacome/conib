<h1 align="center">
  <br>
  Curation of Neurodegeneration in BEL (CONIB)
  <a href="https://travis-ci.com/pharmacome/conib">
    <img src="https://travis-ci.com/pharmacome/conib.svg?branch=master"
         alt="Travis CI">
  </a>
  <a href="https://zenodo.org/badge/latestdoi/159803376">
  	<img src="https://zenodo.org/badge/159803376.svg" alt="DOI">
  </a>
  <br>
</h1>

<p align="center">
This knowledge repository, developed during the <a href="https://pharmacome.github.io">Human Brain Pharmacome project</a>, contains documents in Biological Expression Language (BEL) describing neurodegenerative disease phenomena such as tauopathies.
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

## Content

- [hbp_knowledge](https://github.com/pharmacome/conib/tree/master/hbp_knowledge): This folder contains curated BEL
  documents. Most have been organized by category (protein of interest, biological process of interest, pathway, etc.).
  Almost BEL documents correspond to a single publication, but a select few contain content from several due to
  topic-based curation.
- [docs](https://github.com/pharmacome/conib/tree/master/docs): This folder contains automatically generated HTML
  summaries of the content that can best be accesed through https://pharmacome.github.io/conib.
- [notebooks](https://github.com/pharmacome/conib/tree/master/notebooks): This folder contains various Jupyter
  notebooks associated with the repository. Since many of them use PyBEL-Jupyter, they may be best viewed using
  [NBViewer](https://nbviewer.jupyter.org/github/pharmacome/conib/tree/master/notebooks/).

### Curation Planning

Here are a few links for navigating the GitHub issues and pull requests:

- [Pull requests for curation](https://github.com/pharmacome/conib/pulls?q=is%3Apr+is%3Aopen+label%3ACuration)
- [Pull requests for recuration approved by a reviewer](https://github.com/pharmacome/conib/pulls?q=is%3Apr+is%3Aopen+review%3Aapproved+label%3ARecuration)

## Installation

``hbp_knowledge`` can be installed from [PyPI](https://pypi.org/project/hbp-knowledge/) with the following command:

```bash
$ pip install hbp_knowledge
```

or the latest version can be installed from [GitHub](https://github.com/pharmacome/conib) with:

```bash
$ pip install git+https://github.com/pharmacome/conib.git
```

## Usage

The graph can be loaded with:

```python
import hbp_knowledge

# Get a dictionary of names to graphs
graphs = hbp_knowledge.get_graphs()

# Get all BEL documents as a single graph
graph = hbp_knowledge.get_graph()
```

## Contributing

Contributions are welcome! Please submit all pull requests to https://github.com/pharmacome/conib.

## License

- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.
