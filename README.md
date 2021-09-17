create virtual environment

```bash
conda create -n wenv python=3.7 -y
```

activate virtual environment

```bash
conda activate wenv
```

create requirment.txt

```bash
'' > requirement.txt
```

install requirments

```bash
pip install -r requirement.txt
```

Create data_given folder as data source from client and paste data

```bash
mkdir data_given
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit MLOPS"
```

install tox and pytest

- to perform testing

create tox.ini file

```bash
'' > tox.ini

```

create test folder to keep test scripts

```bash
mkdir tests/conftest.py tests/test_conf.py

```

run tox using below command

```bash
tox

```

for tox rebulding

```bash

tox -r

```

to run test scripts

```bash
pytest -v
```

#### to build own package PyPi

create setup.py file

```bash

pip install -e .
```

to create wheel

```bash
python setup.py sdist bdist_wheel

```
