# CoSt
 
This repository contains the codes and data associated with the following manuscript:<br>
<i>Composition structures and biologically meaningful logics: plausibility and relevance in bipartite models of gene regulation.</i><br>
Yasharth Yadav#, Ajay Subbaroyan#, Olivier C. Martin*, Areejit Samal*.<br>
(# Equal contribution, * Corresponding author)<br>

The repository is organized in two folders, which are described below. 

## 1. CODE

- **BF_compositions.py**: Python script to enumerate the distinct composed BFs possible under a given composition structure, after accounting for all the permutations of the inputs. Many of the codes used in this script were borrowed from the following GitHub repository: https://github.com/asamallab/MCBF

- **composed_BF_catalog**: Folder containing individual files with a list of already generated composed BFs upto <i>k=5</i> inputs.

## 2. DATA

Contains information about the ChIP-seq IDR narrowPeak bed files for transcription factor binding sites acquired from the [ENCODE project](https://www.encodeproject.org).

- **ChIP-seq-list-HepG2.tsv**: We acquired unique ChIP-seq IDR narrowPeak bed files for 458 transcription factors in the HepG2 cell line in *Homo sapiens*.

- **ChIP-seq-list-K562.tsv**: We acquired unique ChIP-seq IDR narrowPeak bed files for 323 transcription factors in the K562 cell line in *Homo sapiens*.

Note that we have also used a separate dataset of active enhancer regions from the following source:

"STARRPeaker: uniform processing and accurate identification of STARR-seq active regions". Donghoon Lee *et al.* 2020 <br>
[Link to the active enhancer dataset for both HepG2 and K562 cell lines](https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-020-02194-x/MediaObjects/13059_2020_2194_MOESM2_ESM.xlsx)
