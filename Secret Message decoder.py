def is_not_valid(a):
    '''
    Goes through all the characters in a string. If one of the characters \
    is not a letter or space character, returns true. Else it returns False.
    Parameters:
        a(string): user input
    Returns:
        (boolean): result of whether the length of string is a square number
    Examples:
    >>> is_not_valid('Hello0w rld45')
    True
    >>> is_not_valid('Hey I am Sara')
    False
    >>> is_not_valid('123456')
    True
    '''
    for char in a:
        ascii_value = ord(char)
        #Comparing characters with ascii values to see if conditions are met
        if not (65<= ascii_value <=90 or 97<= ascii_value <= 122 or
                ascii_value == 32):
            return True
    else:
        return False


def is_not_square(b):
    '''
    Checks whether the length of a string is a squared number
    Parameters:
        b(string): user input
    Returns:
        (boolean): result of whether the length of string is a square number
    Examples:
        >>> is_not_square('abcdefghi')
        False
        >>> is_not_square('1234567891')
        True
        >>> is_not_square('lmno')
        False
        
    '''
    length = len(b)
    i = 1
    while length >= i * i:
        if i * i == length:
            return False
        i += 1
    return True


def string2list(c):
    '''
    Converts a string that only contains letters and spaces into a list
    Parameters:
        c(string): user input
    Returns:
        (list): elements of the string in a 2D square list
    Examples:
    >>> string2list('abcdefghi') 
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    >>> string2list('check this')
    []
    >>> string2list('hello bye')
    [['h', 'e', 'l'], ['l', 'o', ' '], ['b', 'y', 'e']] 
    '''
    #Checking string validity
    if is_not_valid(c) or is_not_square(c) or not 1<= len(c) <= 1000:
        return []
    n = 1
    while n * n < len(c):
        n+=1

    if n * n != len(c):
        return[]
    #Creating 2d list
    result = []
    for i in range(0,len(c),n):
        row = list(c[i:i + n])
        result.append(row)
    return result


def add_space(input_text):
    '''
    Takes a string input and returns another string with the same input
    but adds a space whenever an upper case letter is between
    two lowercase letters.
    Parameters:
        input_text(string): user input
    Returns:
        output_text(string): same elements as input_string with spaces where specified
    Examples:
    >>> add_space('howAreYou')
    'how Are You'
    >>> add_space('bAc')
    'A'
    >>> add_space('thisISaTest')
    'thisISa Test'
    '''
    result = []
    for i in range(len(input_text)):
        #Checking if an uppercase letter is between two lowercase letters, add space if true
        if (i > 0 and i < len(input_text) -1 and input_text[i].isupper()
            and input_text[i - 1].islower() and input_text[i + 1].islower()):
            result.append(' ')
            
        result.append(input_text[i])
        output_text = ''.join(result)
    return output_text


def list2string(list):
    '''
    Converts 2D lists into a string going from top to bottom, left to right.
    Also calls add_space to add spaces where necessary.
    Parameters:
        (list): list given by user
    Returns:
        None(NoneType)
    Examples:
    >>> list2string([['H', 'e', 'l'], ['l', 'o', 'o '], ['B', 'y', 'e']])
    'Helloo Bye'
    >>> list2string([['a', 'b', 'c'], ['D', 'e', 'f'], ['g', 'H', 'i']])
    'abc Defg Hi'
    >>> list2string([['T', 'e', 's'], ['t', 'I', 'n'], ['g', ' ', '1']])
    'Test Ing 1'
    '''
    # converting list into string
    result = ""
    for row in list:
        # joining row characters and adding them to result
        result += ''.join(row)
    return add_space(result)


def horizontal_flip(input_list):
    '''
    Horizontally flips the list given by user.
    Parameters:
        input_list(list): list given by user
    Returns:
        (list): input_list swapped horizontally
    Examples:
    >>> input_list = [['H', 'e', 'l'], ['l', 'o', 'o '], ['B', 'y', 'e']]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['l', 'e', 'H'], ['o ', 'o', 'l'], ['e', 'y', 'B']]
    >>> input_list = [['T', 'e', 's'], ['t', 'I', 'n'], ['g', ' ', '1']]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['s', 'e', 'T'], ['n', 'I', 't'], ['1', ' ', 'g']]
    >>> input_list = [['f', 'i', 's'], ['h', 'I', 'n'], ['g', ' ', '2']]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['s', 'i', 'f'], ['n', 'I', 'h'], ['2', ' ', 'g']]
    '''
    for row in input_list:
        # swapping elements for each row to flip horizontally
        for i in range(len(row) // 2):
            # swapping elements at index i and len(row) - 1 - i
            row[i], row[len(row) - 1 - i] = row[len(row) - 1 - i], row[i]


def transpose(input_list):
    '''
    Transposes a 2D square list 
    Parameters:
        input_list(list): list given by user
    Returns:
        None(NoneType)
    Examples:
    >>> input_list = [['H', 'e', 'l'], ['l', 'o', 'o '], ['B', 'y', 'e']]
    >>> transpose(input_list)
    >>> input_list
    [['H', 'l', 'B'], ['e', 'o', 'y'], ['l', 'o ', 'e']]
    >>> input_list = [['a', 'b', 'c'], ['D', 'e', 'f'], ['g', 'H', 'i']]
    >>> transpose(input_list)
    >>> input_list
    [['a', 'D', 'g'], ['b', 'e', 'H'], ['c', 'f', 'i']]
    >>> input_list = [['T', 'e', 's'], ['t', 'I', 'n'], ['g', ' ', '1']]
    >>> transpose(input_list)
    >>> input_list
    [['T', 't', 'g'], ['e', 'I', ' '], ['s', 'n', '1']]
    '''
    n = len(input_list)
    # transpose the matrix 
    for i in range(n):
        for j in range(i + 1, n): 
            # swapping the element at (i, j) with the element at (j, i)
            input_list[i][j], input_list[j][i] = input_list[j][i], input_list[i][j]


def flip_list(input_list):
    '''
    Flips a 2D square list by performing a horizontal flip and then transposing it
    Parameters:
        input_list (list): 2D square list to be transformed.
    Returns:
        None(NoneType)
    Examples:
    >>> input_list = [['H', 'e', 'l'], ['l', 'o', 'o '], ['B', 'y', 'e']]
    >>> fliplist(input_list)
    >>> input_list
    [['B', 'y', 'e'], ['l', 'o', 'o '], ['H', 'e', 'l']]
    >>> input_list = [['H', 'l', 'W'], ['e', 'd', 'o'], ['y', ' ', 'r']]
    >>> flip_list(input_list)
    >>> input_list
    [['W', 'o', 'r'], ['l', 'd', ' '], ['H', 'e', 'y']]
    >>> input_list = [['H', 'i', 'I'], ['e', 'a', 'n'], ['y', ' ', 'd']]
    >>> flip_list(input_list)
    >>> input_list
    [['I', 'n', 'd'], ['i', 'a', ' '], ['H', 'e', 'y']]
    '''
    horizontal_flip(input_list)
    transpose(input_list)
    

def decipher_code(input_string):
    '''
    Deciphers the input string by processing each sentence. Each sentence is converted to a list, 
    flipped using the fliplist function, and then converted back to a string. Invalid sentences 
    containing numbers or special characters are ignored.

    Parameters:
        input_string (str): The string to be deciphered.

    Returns:
        (string): The deciphered string with all valid sentences.
    Examples:
    >>> decipher_code('BlHyoee l')
    'Hello Bye'
    
    
    '''
    sentences = input_string.split('.')
    deciphered_sentences = []
    for sentence in sentences:
        # Check if the sentence is valid 
        if not is_not_valid(sentence) and sentence != '':
            sentence_2d = string2list(sentence)
            
            # Process the sentence only if string2list returned a valid 2D list
            if sentence_2d:
                flip_list(sentence_2d)
                deciphered_sentence = list2string(sentence_2d)
                deciphered_sentences.append(deciphered_sentence)
    
    result = '. '.join(deciphered_sentences)
    if input_string and input_string[-1] == '.':
        result += '.'
    
    return result
