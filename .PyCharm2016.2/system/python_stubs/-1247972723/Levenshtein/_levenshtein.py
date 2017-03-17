# encoding: utf-8
# module Levenshtein._levenshtein
# from /usr/lib/python2.7/dist-packages/Levenshtein/_levenshtein.x86_64-linux-gnu.so
# by generator 1.143
"""
A C extension module for fast computation of:
- Levenshtein (edit) distance and edit sequence manipulation
- string similarity
- approximate median strings, and generally string averaging
- string sequence and set similarity

Levenshtein has a some overlap with difflib (SequenceMatcher).  It
supports only strings, not arbitrary sequence types, but on the
other hand it's much faster.

It supports both normal and Unicode strings, but can't mix them, all
arguments to a function (method) have to be of the same type (or its
subclasses).
"""
# no imports

# functions

def apply_edit(edit_operations, source_string, destination_string): # real signature unknown; restored from __doc__
    """
    Apply a sequence of edit operations to a string.
    
    apply_edit(edit_operations, source_string, destination_string)
    
    In the case of editops, the sequence can be arbitrary ordered subset
    of the edit sequence transforming source_string to destination_string.
    
    Examples:
    
    >>> e = editops('man', 'scotsman')
    >>> apply_edit(e, 'man', 'scotsman')
    'scotsman'
    >>> apply_edit(e[:3], 'man', 'scotsman')
    'scoman'
    
    The other form of edit operations, opcodes, is not very suitable for
    such a tricks, because it has to always span over complete strings,
    subsets can be created by carefully replacing blocks with 'equal'
    blocks, or by enlarging 'equal' block at the expense of other blocks
    and adjusting the other blocks accordingly.
    
    Examples:
    >>> a, b = 'spam and eggs', 'foo and bar'
    >>> e = opcodes(a, b)
    >>> apply_edit(inverse(e), b, a)
    'spam and eggs'
    >>> e[4] = ('equal', 10, 13, 8, 11)
    >>> a, b, e
    >>> apply_edit(e, a, b)
    'foo and ggs'
    """
    pass

def distance(string1, string2): # real signature unknown; restored from __doc__
    """
    Compute absolute Levenshtein distance of two strings.
    
    distance(string1, string2)
    
    Examples (it's hard to spell Levenshtein correctly):
    
    >>> distance('Levenshtein', 'Lenvinsten')
    4
    >>> distance('Levenshtein', 'Levensthein')
    2
    >>> distance('Levenshtein', 'Levenshten')
    1
    >>> distance('Levenshtein', 'Levenshtein')
    0
    
    Yeah, we've managed it at last.
    """
    pass

def editops(source_string, destination_string): # real signature unknown; restored from __doc__
    """
    Find sequence of edit operations transforming one string to another.
    
    editops(source_string, destination_string)
    editops(edit_operations, source_length, destination_length)
    
    The result is a list of triples (operation, spos, dpos), where
    operation is one of 'equal', 'replace', 'insert', or 'delete';  spos
    and dpos are position of characters in the first (source) and the
    second (destination) strings.  These are operations on signle
    characters.  In fact the returned list doesn't contain the 'equal',
    but all the related functions accept both lists with and without
    'equal's.
    
    Examples:
    
    >>> editops('spam', 'park')
    [('delete', 0, 0), ('insert', 3, 2), ('replace', 3, 3)]
    
    The alternate form editops(opcodes, source_string, destination_string)
    can be used for conversion from opcodes (5-tuples) to editops (you can
    pass strings or their lengths, it doesn't matter).
    """
    pass

def hamming(string1, string2): # real signature unknown; restored from __doc__
    """
    Compute Hamming distance of two strings.
    
    hamming(string1, string2)
    
    The Hamming distance is simply the number of differing characters.
    That means the length of the strings must be the same.
    
    Examples:
    >>> hamming('Hello world!', 'Holly grail!')
    7
    >>> hamming('Brian', 'Jesus')
    5
    """
    pass

def inverse(edit_operations): # real signature unknown; restored from __doc__
    """
    Invert the sense of an edit operation sequence.
    
    inverse(edit_operations)
    
    In other words, it returns a list of edit operations transforming the
    second (destination) string to the first (source).  It can be used
    with both editops and opcodes.
    
    Examples:
    
    >>> inverse(editops('spam', 'park'))
    [('insert', 0, 0), ('delete', 2, 3), ('replace', 3, 3)]
    >>> editops('park', 'spam')
    [('insert', 0, 0), ('delete', 2, 3), ('replace', 3, 3)]
    """
    pass

def jaro(string1, string2): # real signature unknown; restored from __doc__
    """
    Compute Jaro string similarity metric of two strings.
    
    jaro(string1, string2)
    
    The Jaro string similarity metric is intended for short strings like
    personal last names.  It is 0 for completely different strings and
    1 for identical strings.
    
    Examples:
    >>> jaro('Brian', 'Jesus')
    0.0
    >>> jaro('Thorkel', 'Thorgier')  # doctest: +ELLIPSIS
    0.779761...
    >>> jaro('Dinsdale', 'D')  # doctest: +ELLIPSIS
    0.708333...
    """
    pass

def jaro_winkler(string1, string2, prefix_weight=None): # real signature unknown; restored from __doc__
    """
    Compute Jaro string similarity metric of two strings.
    
    jaro_winkler(string1, string2[, prefix_weight])
    
    The Jaro-Winkler string similarity metric is a modification of Jaro
    metric giving more weight to common prefix, as spelling mistakes are
    more likely to occur near ends of words.
    
    The prefix weight is inverse value of common prefix length sufficient
    to consider the strings *identical*.  If no prefix weight is
    specified, 1/10 is used.
    
    Examples:
    
    >>> jaro_winkler('Brian', 'Jesus')
    0.0
    >>> jaro_winkler('Thorkel', 'Thorgier')  # doctest: +ELLIPSIS
    0.867857...
    >>> jaro_winkler('Dinsdale', 'D')  # doctest: +ELLIPSIS
    0.7375...
    >>> jaro_winkler('Thorkel', 'Thorgier', 0.25)
    1.0
    """
    pass

def matching_blocks(edit_operations, source_length, destination_length): # real signature unknown; restored from __doc__
    """
    Find identical blocks in two strings.
    
    matching_blocks(edit_operations, source_length, destination_length)
    
    The result is a list of triples with the same meaning as in
    SequenceMatcher's get_matching_blocks() output.  It can be used with
    both editops and opcodes.  The second and third arguments don't
    have to be actually strings, their lengths are enough.
    
    Examples:
    
    >>> a, b = 'spam', 'park'
    >>> matching_blocks(editops(a, b), a, b)
    [(1, 0, 2), (4, 4, 0)]
    >>> matching_blocks(editops(a, b), len(a), len(b))
    [(1, 0, 2), (4, 4, 0)]
    
    The last zero-length block is not an error, but it's there for
    compatibility with difflib which always emits it.
    
    One can join the matching blocks to get two identical strings:
    >>> a, b = 'dog kennels', 'mattresses'
    >>> mb = matching_blocks(editops(a,b), a, b)
    >>> ''.join([a[x[0]:x[0]+x[2]] for x in mb])
    'ees'
    >>> ''.join([b[x[1]:x[1]+x[2]] for x in mb])
    'ees'
    """
    pass

def median(string_sequence, weight_sequence=None): # real signature unknown; restored from __doc__
    """
    Find an approximate generalized median string using greedy algorithm.
    
    median(string_sequence[, weight_sequence])
    
    You can optionally pass a weight for each string as the second
    argument.  The weights are interpreted as item multiplicities,
    although any non-negative real numbers are accepted.  Use them to
    improve computation speed when strings often appear multiple times
    in the sequence.
    
    Examples:
    
    >>> median(['SpSm', 'mpamm', 'Spam', 'Spa', 'Sua', 'hSam'])
    'Spam'
    >>> fixme = ['Levnhtein', 'Leveshein', 'Leenshten',
    ...          'Leveshtei', 'Lenshtein', 'Lvenstein',
    ...          'Levenhtin', 'evenshtei']
    >>> median(fixme)
    'Levenshtein'
    
    Hm.  Even a computer program can spell Levenshtein better than me.
    """
    pass

def median_improve(string, string_sequence, weight_sequence=None): # real signature unknown; restored from __doc__
    """
    Improve an approximate generalized median string by perturbations.
    
    median_improve(string, string_sequence[, weight_sequence])
    
    The first argument is the estimated generalized median string you
    want to improve, the others are the same as in median().  It returns
    a string with total distance less or equal to that of the given string.
    
    Note this is much slower than median().  Also note it performs only
    one improvement step, calling median_improve() again on the result
    may improve it further, though this is unlikely to happen unless the
    given string was not very similar to the actual generalized median.
    
    Examples:
    
    >>> fixme = ['Levnhtein', 'Leveshein', 'Leenshten',
    ...          'Leveshtei', 'Lenshtein', 'Lvenstein',
    ...          'Levenhtin', 'evenshtei']
    >>> median_improve('spam', fixme)
    'enhtein'
    >>> median_improve(median_improve('spam', fixme), fixme)
    'Levenshtein'
    
    It takes some work to change spam to Levenshtein.
    """
    pass

def opcodes(source_string, destination_string): # real signature unknown; restored from __doc__
    """
    Find sequence of edit operations transforming one string to another.
    
    opcodes(source_string, destination_string)
    opcodes(edit_operations, source_length, destination_length)
    
    The result is a list of 5-tuples with the same meaning as in
    SequenceMatcher's get_opcodes() output.  But since the algorithms
    differ, the actual sequences from Levenshtein and SequenceMatcher
    may differ too.
    
    Examples:
    
    >>> for x in opcodes('spam', 'park'):
    ...     print(x)
    ...
    ('delete', 0, 1, 0, 0)
    ('equal', 1, 3, 0, 2)
    ('insert', 3, 3, 2, 3)
    ('replace', 3, 4, 3, 4)
    
    The alternate form opcodes(editops, source_string, destination_string)
    can be used for conversion from editops (triples) to opcodes (you can
    pass strings or their lengths, it doesn't matter).
    """
    pass

def quickmedian(string, weight_sequence=None): # real signature unknown; restored from __doc__
    """
    Find a very approximate generalized median string, but fast.
    
    quickmedian(string[, weight_sequence])
    
    See median() for argument description.
    
    This method is somewhere between setmedian() and picking a random
    string from the set; both speedwise and quality-wise.
    
    Examples:
    
    >>> fixme = ['Levnhtein', 'Leveshein', 'Leenshten',
    ...          'Leveshtei', 'Lenshtein', 'Lvenstein',
    ...          'Levenhtin', 'evenshtei']
    >>> quickmedian(fixme)
    'Levnshein'
    """
    pass

def ratio(string1, string2): # real signature unknown; restored from __doc__
    """
    Compute similarity of two strings.
    
    ratio(string1, string2)
    
    The similarity is a number between 0 and 1, it's usually equal or
    somewhat higher than difflib.SequenceMatcher.ratio(), because it's
    based on real minimal edit distance.
    
    Examples:
    
    >>> ratio('Hello world!', 'Holly grail!')  # doctest: +ELLIPSIS
    0.583333...
    >>> ratio('Brian', 'Jesus')
    0.0
    
    Really?  I thought there was some similarity.
    """
    pass

def seqratio(string_sequence1, string_sequence2): # real signature unknown; restored from __doc__
    """
    Compute similarity ratio of two sequences of strings.
    
    seqratio(string_sequence1, string_sequence2)
    
    This is like ratio(), but for string sequences.  A kind of ratio()
    is used to to measure the cost of item change operation for the
    strings.
    
    Examples:
    
    >>> seqratio(['newspaper', 'litter bin', 'tinny', 'antelope'],
    ...          ['caribou', 'sausage', 'gorn', 'woody'])
    0.21517857142857144
    """
    pass

def setmedian(string, weight_sequence=None): # real signature unknown; restored from __doc__
    """
    Find set median of a string set (passed as a sequence).
    
    setmedian(string[, weight_sequence])
    
    See median() for argument description.
    
    The returned string is always one of the strings in the sequence.
    
    Examples:
    
    >>> setmedian(['ehee', 'cceaes', 'chees', 'chreesc',
    ...            'chees', 'cheesee', 'cseese', 'chetese'])
    'chees'
    
    You haven't asked me about Limburger, sir.
    """
    pass

def setratio(string_sequence1, string_sequence2): # real signature unknown; restored from __doc__
    """
    Compute similarity ratio of two strings sets (passed as sequences).
    
    setratio(string_sequence1, string_sequence2)
    
    The best match between any strings in the first set and the second
    set (passed as sequences) is attempted.  I.e., the order doesn't
    matter here.
    
    Examples:
    
    >>> setratio(['newspaper', 'litter bin', 'tinny', 'antelope'],
    ...          ['caribou', 'sausage', 'gorn', 'woody'])  # doctest: +ELLIPSIS
    0.281845...
    
    No, even reordering doesn't help the tinny words to match the
    woody ones.
    """
    pass

def subtract_edit(edit_operations, subsequence): # real signature unknown; restored from __doc__
    """
    Subtract an edit subsequence from a sequence.
    
    subtract_edit(edit_operations, subsequence)
    
    The result is equivalent to
    editops(apply_edit(subsequence, s1, s2), s2), except that is
    constructed directly from the edit operations.  That is, if you apply
    it to the result of subsequence application, you get the same final
    string as from application complete edit_operations.  It may be not
    identical, though (in amibuous cases, like insertion of a character
    next to the same character).
    
    The subtracted subsequence must be an ordered subset of
    edit_operations.
    
    Note this function does not accept difflib-style opcodes as no one in
    his right mind wants to create subsequences from them.
    
    Examples:
    
    >>> e = editops('man', 'scotsman')
    >>> e1 = e[:3]
    >>> bastard = apply_edit(e1, 'man', 'scotsman')
    >>> bastard
    'scoman'
    >>> apply_edit(subtract_edit(e, e1), bastard, 'scotsman')
    'scotsman'
    """
    pass

# no classes
