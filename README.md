## notice

for Signate 104: https://signate.jp/competitions/104

## readme

- please put signate_DL_datasets in ./dataset

### using virtualenv

- `python3 -m venv .venv` in spammail
- `source .venv/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`
- run `preprocess.py` to make preprocess data
- run `train.py` to make models

## directry

```
spammail_sample
  |── preprocess.py
  |── train.py
  |── requirements.txt
  |── dataset/
  |     └── (please put datasets)
  └── utils/
        └── del_words.txt
```
