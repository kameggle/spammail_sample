## notice

for Signate 104: https://signate.jp/competitions/104

## readme

- please put signate_DL_datasets in ./dataset/

### using venv

- `python3 -m venv .spam` in spammail_sample
- `source .spam/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`
- run `train_preprocess.py` to make train_preprocess data
- run `train.py` to make models
- run `test_preprocess.py` to make test_preprocess data

## directry

```
spammail_sample
  ├── README.md
  |── requirements.txt
  |── dataset/
  |     └── (please put datasets)
  |── train_preprocess.py
  |── train.py
  |── test_preprocess.py
  └── utils/
        └── del_words.txt
```
