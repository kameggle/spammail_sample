## notice

for Signate 104: https://signate.jp/competitions/104

## readme

- please put signate_DL_datasets in ./dataset/
- before PR, please check this page: https://backlog.com/ja/git-tutorial/pull-request/

### using venv

- `python3 -m venv .spam` in spammail_sample
- `source .spam/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`
- run `python3 train_preprocess.py` to make train_preprocess data
- run `python3 train.py` to make models
- run `python3 test_preprocess.py` to make test_preprocess data

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
