

## Forked from the [official repo](https://github.com/lishuya17/MONN.git) and upgraded the python and torch version for Amper GPU.
Following are the original README:

--- 
## Codes for "MONN: a Multi-Objective Neural Network for Predicting Pairwise Non-Covalent Interactions and Binding Affinities between Compounds and Proteins"

The benchmark dataset described in this paper can be found in ./data/, and the creation of this dataset can be reproduced by the protocol in ./create_dataset/.

Before running the MONN model in ./src/, please first use ./src/preprocessing_and_clustering.py to produce necessary files.

For cross validation, e.g., using IC50 data, new-compound setting and clustering threshold 0.3, run:

```python CPI_train.py IC50 new_compound 0.3```

### Requirements:
Python2.7

rdkit (for preprocessing)

Pytorch >= 0.4.0

scikit-learn

### License

This software is copyrighted by Machine Learning and Computational Biology Group @ Tsinghua University.

The algorithm and data can be used only for NON COMMERCIAL purposes.

---- 
## Notes
### Preset conda environment
```bash
git clone https://github.com/JinyuanSun/MONN.git
cd MONN
conda env create -f environment.yml
conda activate monn
```
### More details about step 3:  
**Step3: calculate the non-covalent interactions between proteins and ligands**  
Extract the non-covalent interactions by using PLIP (https://github.com/ssalentin/plip/)
Put the result files in ./plip_result/
Note: command for using PLIP:   
```bash
python plipcmd.py -f xxx.pdb -t --name xxx_output
```
The `plip` is a good package, relies on openbable, I recommand using docker:  
```bash
docker pull pharmai/plip:latest
docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f 1o41.pdb -t --name output_1o41
```
Also you are welcomed to build it from source code. For some reason, as far as I konw, the conda and pip installation just won't work.  
With docker:
```bash
ls ????.pdb|awk -F "." '{print"docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f "$1".pdb -t --name ../plip_result/output_"$1""}' > job_list.sh
parallel --jobs $num_of_threads < job_list.sh
```
If you managed to install the `plipcmd.py`, run the following in `./pdb_files/`:
```bash
ls ????.pdb|awk -F "." '{print"plipcmd.py -f "$1".pdb -t --name ../plip_result/output_"$1""}' > job_list.sh
parallel --jobs $num_of_threads < job_list.sh
```
Good luck with it!

## Citation
```bibtex
@article{LI2020308,
title = {MONN: A Multi-objective Neural Network for Predicting Compound-Protein Interactions and Affinities},
author = {Shuya Li and Fangping Wan and Hantao Shu and Tao Jiang and Dan Zhao and Jianyang Zeng},
journal = {Cell Systems},
volume = {10},
number = {4},
pages = {308-322.e11},
year = {2020},
issn = {2405-4712},
doi = {https://doi.org/10.1016/j.cels.2020.03.002},
url = {https://www.sciencedirect.com/science/article/pii/S2405471220300818}
}
```

## Warning
**No guarantee of 100% reproduction results in the paper after modifications, if that is what you want, check the official repo!!!**