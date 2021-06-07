import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout
from keras.layers import GlobalMaxPool1D
from keras.models import Model

import click


SAVE_PATH = './model/'
MAX_FEATURES = 20000
MAX_LEN = 250
EMBED_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 5


@click.command()
@click.option('--data_path', '-d', default='./dataset/basedata.csv')
def main(data_path):
    origin_df = pd.read_csv(data_path)
    drop_df = origin_df.dropna()

    y = drop_df['label'].values
    list_sentences = drop_df['mail']

    tokenizer = Tokenizer(num_words=MAX_FEATURES)
    tokenizer.fit_on_texts(list(list_sentences))
    list_tokenized_mails = tokenizer.texts_to_sequences(list_sentences)

    X_train = pad_sequences(list_tokenized_mails, maxlen=MAX_LEN)

    inp = Input(shape=(MAX_LEN, ))
    x = Embedding(MAX_FEATURES, EMBED_SIZE)(inp)
    x = LSTM(60, return_sequences=True, name='lstm_layer')(x)
    x = GlobalMaxPool1D()(x)
    x = Dropout(0.1)(x)
    x = Dense(50, activation="relu")(x)
    x = Dropout(0.1)(x)
    x = Dense(1, activation="sigmoid")(x)

    model = Model(inputs=inp, outputs=x)
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    model.fit(X_train, y, batch_size=BATCH_SIZE,
              epochs=EPOCHS, validation_split=0.3)
    model.save('{}sample_model.h5'.format(SAVE_PATH))


if __name__ == '__main__':
    main()
