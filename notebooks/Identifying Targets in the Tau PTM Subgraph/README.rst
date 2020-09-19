Identifying Targets in the Tau Phosphorylation Subgraph
=======================================================
The files in this folder are:

- ``Get Tau PTM Subgraph and Previously Drugged Targets.ipynb``:
  This Jupyter notebook generates a subgraph based on all of the controllers 
  (kinases and phosphotases) upstream of all post-translationally modified
  variants of the Tau protein. It checks which of those proteins have chemical
  matter in DrugBank listed as "targeting" them, and returns the list.
- ``tau-ptm-pmids.txt``:
  A list of all PubMed identifiers for relationships in this graph
- ``targeted-tau-ptm-controllers.txt``:
  A list of HGNC identifiers and gene symbols of all controllers of
  phosphorylation of Tau that have a drug in DrugBank, as well as
  their target residues on the Tau protein
- ``tau-ptm-article-targets.tsv``:
  A list of all PubMed identifeirs for relationships incident with
  the previously mentioned targets
