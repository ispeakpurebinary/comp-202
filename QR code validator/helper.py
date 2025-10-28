#CONSTANTS
DAY_LENGTH = 2
MONTH_LENGTH = 2
YEAR_LENGTH = 4
VALID_BINARY_CHARS = ['0', '1']

def convert_date(date_str):
    """
    Converts a string in date format into dictionary format
    Parameters:
        date_str(string): date as a string in the format DD/MM/YYYY
    Returns:
       (dict): stores input string values in a dictionary with 'Day','Month,'Year' as keys
    Examples:
    >>> convert_date("04/08/2006")
    {'Day': '04', 'Month': '08', 'Year': '2006'}
    >>> convert_date("00/00")
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    raise ValueError("Input Format Incorrect!")
    ValueError: Input Format Incorrect!
    >>> convert_date("28/11/2024")
    {'Day': '28', 'Month': '11', 'Year': '2024'}
    """
    part = date_str.split('/')
    # Checking if input string meets our criteria
    if len(part) != 3 or len(part[0]) != DAY_LENGTH or len(part[1]) != MONTH_LENGTH \
        or len(part[2]) != YEAR_LENGTH:
        raise ValueError("Input format incorrect!")
    return {"Day":part[0],"Month":part[1],"Year":part[2]}


def get_data(file_path):
    """
    Reads a file and returns a nested list if file contails only 0s and 1s, \
    raises a ValueError if otherwise.
    Parameters:
        file_path(string): The path to the file
    Returns:
        (list): Nested list of 0s and 1s inside the file
    Examples:
    >>> get_data("big_data.txt")
    [[1, 0], [0, 1], [1, 0, 1, 0, 1], [1, 0]]
    >>> get_data("big_data_error.txt")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        raise ValueError("File should contain only 0s and 1s!")
    ValueError: File should contain only 0s and 1s!
    >>> get_data("small_data.txt")
    [[0, 1], [1, 0]]
    """
    nested_list = []
    with open(file_path,'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                # Checking if characters are 0s and 1s
                if char not in VALID_BINARY_CHARS:
                    raise ValueError("File should contain only 0s and 1s!")
                row.append(int(char))
            nested_list.append(row)
    return nested_list
