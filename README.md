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
