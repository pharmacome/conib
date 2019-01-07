<h1 align="center">
  <br>
  HBP Knowledge
  <a href="https://travis-ci.com/pharmacome/knowledge">
    <img src="https://travis-ci.com/pharmacome/knowledge.svg?branch=master"
         alt="Travis CI">
  </a>
  <br>
</h1>

<p align="center">
This repository contains knowledge curated in Biological Expression Language (BEL)
for the Human Brain Pharmacome (HBP) project.
</p>

## Installation

The latest version can be installed form GitHub with:

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

## License

- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.
