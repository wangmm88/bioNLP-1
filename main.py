import os
from nltk.parse import stanford
from nltk import sent_tokenize as stokenize
from collections import namedtuple
from toolz import *
from itertools import *


ddir = '/home/adam/Documents/resources/'
os.environ['STANFORD_PARSER'] = ddir+'stanford-parser-full-2015-04-20/'
os.environ['STANFORD_MODELS'] = ddir+'stanford-parser-full-2015-04-20/'
parser = stanford.StanfordDependencyParser(
    model_path=ddir+"edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
abstract = namedtuple("Article", "title abstract")

def rtail(l):
    return list(islice(l, 1, None))

def read_data(path):
    with open(path) as f:
        text = [x for x in f.read().split('\n') if x]
        return abstract(first(text), stokenize(' '.join(rtail(text))))

def read_dir(dirr):
    return list(map(lambda y: read_data(dirr+y),
                    filter(lambda x: x.endswith('.txt'),
                           os.listdir(dirr))))

def extract_features(item):
    pass

def get_parsed_sentences():
    pass

def main():
    train_dir = '/home/adam/data/bionlp16/ent_categorization/BioNLP-ST-2016_BB-cat_train/'
    articles = read_dir(train_dir)

    #for a in articles:
        #print(a)
    
if __name__ == '__main__':
    main()
