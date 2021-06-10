## notice

for Signate 104: https://signate.jp/competitions/104

## readme

- please put signate_DL_datasets in ./dataset/

### using venv

- `python3 -m venv .venv` in spammail
- `source .venv/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`
- run `train_preprocess.py` to make train_preprocess data
- run `train.py` to make models
- run `test_preprocess.py` to make test_preprocess data

## directry

```
spammail_sample
  |── train_preprocess.py
  |── train.py
  |── test_preprocess.py
  |
  |── requirements.txt
  |
  |── dataset/
  |     └── (please put datasets)
  |
  └── utils/
        └── del_words.txt
```
