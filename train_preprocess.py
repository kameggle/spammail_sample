import glob
import os
import pandas as pd
import re

import click

from utils.nltk_download import make_stopwords

SAVE_PATH = './dataset/'
DEL_WORDS = './utils/del_words.txt'
STOP_WORDS = make_stopwords()


def make_textdict(textfiles, data_path):
    os.makedirs(SAVE_PATH, exist_ok=True)
    del_words = open(DEL_WORDS, 'r', encoding='UTF-8')
    del_list = del_words.read().split('\n')
    del_set = set(del_list)
    text_dict = {}

    for text in textfiles:
        with open(text, mode='r', encoding='utf-8') as mail:
            mail = str.lower(mail.read())
            for i in del_set:
                mail = re.sub(f'.*{i}.*\n', ' ', mail, flags=re.MULTILINE)
            for i in STOP_WORDS:
                mail = re.sub(f' {i} ', ' ', mail, flags=re.MULTILINE)
            mail = re.sub('[^a-z]', ' ', mail, flags=re.MULTILINE)
            mail = re.sub('\n', ' ', mail, flags=re.MULTILINE)
            mail = re.sub(r'\s+', ' ', mail, flags=re.MULTILINE)
            text = re.sub(f'{data_path}', '', text)
            text_dict[text] = mail

    return text_dict


def make_basedata(text_dict, master_path):
    main_df = pd.read_table(master_path)
    text_df = pd.DataFrame(
        text_dict.items(), columns=['file_name', 'mail'])
    merged_df = pd.merge(main_df, text_df, on='file_name')

    return merged_df


def make_csv(merged_df, file_name):
    os.makedirs(SAVE_PATH, exist_ok=True)
    submit_name = '{}{}.csv'.format(SAVE_PATH, file_name)
    merged_df.to_csv(submit_name, index=False)


@click.command()
@click.option('--data_path', '-d', default='./dataset/train2/')
@click.option('--master_path', '-m', default='./dataset/train_master.tsv')
@click.option('--file_name', '-n', default='basedata')
def main(data_path, master_path, file_name):
    text_name = glob.glob('{}*'.format(data_path))
    textfiles = set(text_name)
    text_dict = make_textdict(textfiles, data_path)
    merged_df = make_basedata(text_dict, master_path)
    make_csv(merged_df, file_name)


if __name__ == '__main__':
    main()
