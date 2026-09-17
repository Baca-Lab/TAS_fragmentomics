![branding](.img/baca-lab-branding.jpeg)

## TAS fragmentomics

##### This repository contains Transcriptional Activation Score (TAS) calculation, and nucleosome repeat length simulation.

All development and testing were performed on CentOS 7.9.
The dependencies listed below should install within a few minutes in a standard computing environment.

### Transcriptional Activation Score (TAS) Calculation<br>
This module takes fragment count matrix as input and computes TAS by considering the relationship between correlation between expression (see /correlation matrix ; supplementary table (see reference)) and fragmentation patteren near transcription start site (TSS).

----
#### Dependencies
- Python3
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

## TAS demo

This demo reproduces one of the analyses presented in the main text (**Figure 5f**).
The workflow includes all steps from data download to figure generation.
The demo can be run using:

```bash
bash TAS_demo/run.bash
```
Upon completion, demo_plot.png will be generated in the output directory.


## Nucelosome repeat length simulation<br>
A step-by-step demo is available in the **/NRL_simulation/NRL_demo.ipynb**. Running all cells on a single CPU core takes approximately 1 hour.

#### Dependencies
- Python 3.11.16
- pandas 3.0.5
- numpy 2.4.6
- joblib 1.6.0
- matplotlib 3.11.1
- scikit-optimize 0.10.2
- scipy 1.17.1
- tqdm 4.70.0





