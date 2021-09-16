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

git init

dvc init

dvc add data_given/winequality.csv
