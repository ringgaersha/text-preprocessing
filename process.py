import re                               # untuk pencarian string atau teks dengan menggunakan pola
import nltk
from nltk.corpus import stopwords       # library stopwords
from nltk.stem import PorterStemmer     # library stemming
from nltk.stem import WordNetLemmatizer # library Lemmatize

stp = stopwords.words('english')
stm = PorterStemmer()
lmtz = WordNetLemmatizer()

def lower(text):                    #fungsi lowercase
    return text.lower()

def remove_punctuation(text):       #fungsi remove_punctuation
    text = re.sub(r'[^\w\s]+', ' ', text)
    return text

def remove_stopwords(text):         #fungsi remove stopwords
    text = ' '.join([word for word in text.split() if word not in stp])
    return text

def stem_text(text):                #fungsi stemming
    text = ' '.join([stm.stem(word) for word in text.split()])
    return text

def lemmatize_text(text):           #fungsi lemmatize
    text = ' '.join([lmtz.lemmatize(word) for word in text.split()])
    return text