
import nltk
from nltk.corpus import stopwords
import ssl


def make_stopwords():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('stopwords')
    sw_english = set(stopwords.words('english'))

    return sw_english
