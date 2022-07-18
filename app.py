#Import package flask
from flask import Flask, request, render_template
#Import package text preprocessing (lowercase,remove punctuation, stopword, stemming, lemmatization)
from process import lower, remove_punctuation, remove_stopwords, stem_text, lemmatize_text

#Inisialisasi fungsi flask
app = Flask(__name__,template_folder='template')
app.debug = True

#Atur route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')        #return halaman html

@app.route('/preprocess', methods=['GET', 'POST'])
def preprocess():                               #fungsi untuk preprocessing
    response = request.form                     #mengambil request dari form
    keys = response.keys()
    original_text = request.form['text']
    text = request.form['text']
    if 'lowercase' in keys:
        text = lower(text)
    if 'punct' in keys:
        text = remove_punctuation(text)
    if 'stp' in keys:
        text = remove_stopwords(text)
    if 'stem' in keys:
        if response['stem'] == 'stem':
            text = stem_text(text)
        elif response['stem'] == 'lem':
            text = lemmatize_text(text)
        else:
            pass
    return render_template('output.html', original_text=original_text,text=text)

if __name__ == '__main__':
    app.run()