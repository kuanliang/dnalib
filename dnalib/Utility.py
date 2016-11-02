import re

def only_atcg(test_string):
    '''return True if the test string contain only atcg
    
    Notes: check if all letters are composed of only a, t, c or g
    
    Args:
        test_string (string): e.g. 'atcgatcg'

    Return:
        Boolean:
            True: test_string only contain a, t, c or g
            False: test_string contain other strings
    
    '''
    match = re.match("^[atcg]*$", test_string)
    
    return match is not None