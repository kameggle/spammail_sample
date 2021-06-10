import glob
import pandas as pd
import re

import click

from train_preprocess import make_textdict, make_csv


def make_text_name(text_list, data_path):
    text_name = []
    for i in text_list:
        text = re.sub("{}".format(data_path), "", i)
        text_name.append(text)

    return text_name


def make_test_df(text_name, test_dict):
    name_df = pd.DataFrame(text_name, columns=['file_name'])
    mail_df = pd.DataFrame(
        test_dict.items(), columns=['file_name', 'mail'])
    test_df = pd.merge(name_df, mail_df, on='file_name')

    return test_df


@click.command()
@click.option('--data_path', '-d', default='./dataset/test2/')
@click.option('--file_name', '-n', default='testdata')
def main(data_path, file_name):
    text_list = glob.glob('{}*'.format(data_path))
    test_dict = make_textdict(text_list, data_path)
    text_name = make_text_name(text_list, data_path)
    test_df = make_test_df(text_name, test_dict)
    make_csv(test_df, file_name)


if __name__ == '__main__':
    main()
