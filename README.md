![branding](.img/baca-lab-branding.jpeg)

## TAS fragmentomics

##### This repository contains Transcriptional Activation Score (TAS) calculation, and nucleosome repeat length simulation.


### Transcriptional Activation Score (TAS) Calculation<br>
This module takes fragment count matrix as input and computes TAS by considering the relationship between correlation between expression (see /correlation matrix ; supplementary table (see reference)) and fragmentation patteren near transcription start site (TSS).

----
#### Dependencies
All analyses and tests were conducted in a Linux environment (CentOS 7.9).
- pandas (1.1.5 or later)
- numpy (1.19.2 or later)

#### Quick start
```
python run_tas.py -i ./example_input/example_twod.csv -pe promoter --mode TAS -a False
```
#### Parameters
* -i (--input) : path for an input fragment count matrix. (see example_input/example_twod.csv)<br>fragment must be counted 5bp size bin level.
* -pe (--promoter_or_enhancer) : The target of calculation. A different correlation matrix is used depending on the input.
* -m (--mode) : if you are not sure about TSS, you can run position-free TAS (pfTAS) mode.<br>In this case, In this case, you can aggregate TSS distance-axis. (see /example_input/example_twod.csv)
* -a (--agg) : In the case you are running pfTAS, you can specify you already aggregate TSS distance-axis.

#### Examples
```
python run_tas.py -i ./example_input/example_twod.csv -pe enhancer --mode pfTAS -a False
python run_tas.py -i ./example_input/example_aggregated.csv -pe promoter --mode pfTAS -a True
```


## Nucelosome repeat length simulation<br>
A step-by-step demo is available in the **/NRL_simulation/NRL_demo.ipynb** (Python version 3.9.23). Running all cells takes approximately 1 hour.

#### Dependencies
All analyses and tests were conducted in a Linux environment (CentOS 7.9).
- pandas (2.3.1)
- numpy (2.0.2)
- joblib (1.5.1)
- matplotlib (3.9.4)
- scikit-optimize (0.10.2)
- scipy (1.13.1)
- tqdm (4.67.1)





