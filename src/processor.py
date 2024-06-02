import pandas as pd
import nltk
from textblob import TextBlob
from src.utils import clean_text, count_syllables, count_personal_pronouns

nltk.download('punkt')

stopwords_files = [
    'StopWords/StopWords_Auditor.txt',
    'StopWords/StopWords_Currencies.txt',
    'StopWords/StopWords_DatesandNumbers.txt',
    'StopWords/StopWords_Generic.txt',
    'StopWords/StopWords_GenericLong.txt',
    'StopWords/StopWords_Geographic.txt',
    'StopWords/StopWords_Names.txt'
]

custom_stopwords = set()
for file in stopwords_files:
    with open(file, 'r') as f:
        for line in f:
            custom_stopwords.add(line.strip().lower())

positive_words = set(open('MasterDictionary/positive-words.txt').read().split())
negative_words = set(open('MasterDictionary/negative-words.txt').read().split())

def analyze_text(row):
    cleaned_text = clean_text(row['text'])
    blob = TextBlob(cleaned_text)
    
    sentences = nltk.sent_tokenize(row['text'])
    words = nltk.word_tokenize(row['text'])
    filtered_words = [word for word in words if word.lower() not in custom_stopwords]
    word_count = len(filtered_words)
    
    positive_score = sum(1 for word in filtered_words if word in positive_words)
    negative_score = sum(1 for word in filtered_words if word in negative_words)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    avg_sentence_length = word_count / len(sentences) if len(sentences) else 0
    
    complex_word_count = sum(1 for word in filtered_words if count_syllables(word) > 2)
    complex_word_percentage = (complex_word_count / word_count) * 100 if word_count else 0
    
    fog_index = 0.4 * (avg_sentence_length + complex_word_percentage) if avg_sentence_length else 0
    avg_words_per_sentence = word_count / len(sentences) if len(sentences) else 0
    
    syllable_count = sum(count_syllables(word) for word in filtered_words)
    personal_pronoun_count = count_personal_pronouns(cleaned_text)
    avg_word_length = sum(len(word) for word in filtered_words) / word_count if word_count else 0
    
    return {
        'URL_ID': row['URL_ID'],
        'URL': row['url'],
        'POSITIVE SCORE': positive_score,
        'NEGATIVE SCORE': negative_score,
        'POLARITY SCORE': polarity_score,
        'SUBJECTIVITY SCORE': subjectivity_score,
        'AVG SENTENCE LENGTH': avg_sentence_length,
        'PERCENTAGE OF COMPLEX WORDS': complex_word_percentage,
        'FOG INDEX': fog_index,
        'AVG NUMBER OF WORDS PER SENTENCE': avg_words_per_sentence,
        'COMPLEX WORD COUNT': complex_word_count,
        'WORD COUNT': word_count,
        'SYLLABLE PER WORD': syllable_count / word_count if word_count else 0,
        'PERSONAL PRONOUNS': personal_pronoun_count,
        'AVG WORD LENGTH': avg_word_length
    }

def process_data(input_file, output_file):
    df = pd.read_csv(input_file)
    x = pd.read_excel('Input.xlsx')
    df["URL_ID"] = x["URL_ID"]
    
    output_structure = pd.read_excel("Output Data Structure.xlsx")
    
    output_data = df.apply(lambda row: analyze_text(row), axis=1)
    output_df = pd.DataFrame(output_data.tolist())
    
    output_df = output_df[output_structure.columns]
    output_df.to_excel(output_file, index=False)
    
    print(f"Textual analysis completed and data saved to {output_file}.")
