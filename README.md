# CoSt
 
This repository contains the codes and data associated with the following manuscript:<br>
<i>Composition structures and biologically meaningful logics: plausibility and relevance in bipartite models of gene regulation.</i><br>
Yasharth Yadav#, Ajay Subbaroyan#, Olivier C. Martin*, Areejit Samal*.<br>
(# Equal contribution, * Corresponding author)<br>

The repository is organized in two folders, which are described below. 

## 1. CODE
 
- **BF_compositions.py**: Python script to enumerate the distinct composed BFs possible under a given composition structure, after accounting for all the permutations of the inputs. Many of the codes used in this script were borrowed from the following GitHub repository: https://github.com/asamallab/MCBF

- **Generate_figures.ipynb**: Jupyter Notebook containing the codes necessary to reproduce the main and supplementary figures of the manuscript. Note that generating certain figures requires additional Python packages. The Shell script commands for installing these packages are provided at the start of the Jupyter notebook.

**NOTE**: Certain codes in the above script require data files as inputs which are provided in the [DATA](https://github.com/asamallab/CoSt/tree/main/DATA) folder. Therefore, to ensure that all the codes run without errors, please download the entire repository without altering the relative paths of the scripts and the data files.

## 2. DATA

- **composed_BF_catalog**: Folder containing individual files with a list of already generated composed BFs upto <i>k=5</i> inputs.

- **ChIP-seq-list-HepG2.tsv**: List of unique ChIP-seq IDR narrowPeak bed filenames for 458 transcription factors in the HepG2 cell line in *Homo sapiens* acquired from the [ENCODE project](https://www.encodeproject.org).

- **ChIP-seq-list-K562.tsv**: List of unique ChIP-seq IDR narrowPeak bed filenames for 323 transcription factors in the K562 cell line in *Homo sapiens* acquired from the [ENCODE project](https://www.encodeproject.org).

- **hepg2_encode_enh_treg.tsv**: List of active enhancers in the HepG2 cell line and the ChIP-seq IDR narrowPeak bed filenames corresponding to the transcription factors that bind to a given active enhancer.

- **k562_encode_enh_treg.tsv**: List of active enhancers in the K562 cell line and the ChIP-seq IDR narrowPeak bed filenames corresponding to the transcription factors that bind to a given active enhancer.

**NOTE**: We have also used a separate [dataset of active enhancer regions](https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-020-02194-x/MediaObjects/13059_2020_2194_MOESM2_ESM.xlsx) from the following paper:

Lee, D., Shi, M., Moran, J. et al. STARRPeaker: uniform processing and accurate identification of STARR-seq active regions. Genome Biol 21, 298 (2020). https://doi.org/10.1186/s13059-020-02194-x <br>
