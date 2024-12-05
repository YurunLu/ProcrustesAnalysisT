# ProcrustesAnalysisT
## A procrustes approach for quantitatively evaluate the similarity of genes and geography following Wang C. et al.
### Usage
#### Input preparation
`PCA.data.txt` in the same direction, with at least four columns, `pc1` and `pc2` for PCA results, `latitude` and `longitude` for the geographic coordinates.
#### Run
`python ./Calculate_T_stat.py`
#### Output
Outputs including 
```
t = {t_statistics} theta = {rotation angle}
p = {p_val} After 10000 permutations
```
and `Distribution_t0_Permutations.pdf` for a hist plot of t_statistics during permutations.

*Reference:* Wang C, Szpiech ZA, Degnan JH, Jakobsson M, Pemberton TJ, Hardy JA, Singleton AB, Rosenberg NA. Comparing spatial maps of human population-genetic variation using Procrustes analysis. Stat Appl Genet Mol Biol. 2010;9(1):Article 13. doi: 10.2202/1544-6115.1493. Epub 2010 Jan 27. PMID: 20196748; PMCID: PMC2861313.
