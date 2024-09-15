# __plancor_ai__
### A model to find the decor that matches your room the best, powered by plancor
<br>

## Installation

1. Clone the repository to your local machine

``` bash
git clone https://github.com/bakayu/plancor_ai.git
cd plancor_ai
```
<br>

2. Depending upon the environment, download the dependency set:
    - Conda (recommended)
       - Download and Install miniforge3 from [here](https://github.com/conda-forge/miniforge) for your operating system.
       - Run the following command to create a conda environment
         ``` bash
         conda env create -f environment.yml
         ```
       - Activate the conda envrionment
         ``` bash
         conda activate plancor
         ```
    - System-wide, make sure that python version installed is <= v3.11
        - Run the following command to install the dependencies
         ``` bash
         pip install -r requirements.txt
         ```
## Usage

1. Run the following command to start the mode.
``` bash
python3 app.py
```
2. open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) on your browser to access the model.
