from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from Utility import only_atcg


def vectorize_fasta(fasta_list):
    '''Transform a fasta list to a numpy array
    
    Notes:
    
    Args:
    
    Return:
    
    '''
    # initialize vectorizer that can count frequencies according to overlapping characters
    atcg_vectorizer = CountVectorizer(analyzer='char', ngram_range=(8, 8))
    # 
    mer8 = atcg_vectorizer.fit_transform(fasta_list)
    # get the numpy array
    mer8_array = mer8.toarray()
    # get feature names
    feature_names = atcg_vectorizer.get_feature_names()
    
    # filter numpy array and featire names
    # first get a boolean list indicate True or False for each indexes
    boolean_array = np.array([True if only_atcg(name) else False for name in feature_names])
    mer8_filtered = mer8_array[:,boolean_array]
    feature_filtered = np.array(feature_names)[boolean_array]
    
    return mer8_filtered, feature_filtered
    
    
    
    
    
    