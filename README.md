# Requirements

You should have Python installed and either activate the virtual environment ```venv```:

```bash
$ source venv/bin/activate
```
or create one and install the requirements:

```bash
$ python -m pip install -r requirements.txt
```

# File description

- ```assessment.txt```: description of the task;
- ```Housing.csv```: dataset file;
- ```assessment.ipynb```: Jupyter Notebook with all the steps to train the model;
- ```pipeline.pkl```: the Linear Regression pipeline;
- ```tests.py```: file containing the unit tests;
- ```utils.py```: file containing the requested functions;

# Testing

To run the test suite:
```bash
$ python test.py
```
