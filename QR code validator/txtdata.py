import copy
from helper import get_data

#Constants
BLOCK_CHAR = "\u2588\u2588"

class TxtData:
    '''
    Represents a 2D grid of binary data with operations for analysis, saving, and comparison.
    Instance Attributes:
        data (list): A nested list of integers representing the binary grid.
        rows (int): Number of rows in the binary grid.
        cols (int): Number of columns in the binary grid.
        '''

    def __init__(self, data):
        '''
        Creates a deep copy of input data initialises values.
        Parameters:
            data (list): Input 2D nested list.
        Returns:
            None (NoneType)
        Examples:
        >>> new_list = [[1, 2, 3, 4], [4, 5, 6, 7, 8]]
        >>> my_txt_new = TxtData(new_list)
        >>> my_txt_new.rows
        2
        >>> my_txt_new.cols
        4
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.rows
        33
        >>> my_txt.cols
        33
        >>> list2 = [[7,8,6,4],[8,3,9,2,6],[3,5,0,1]]
        >>> my_txt_new = TxtData(list2)
        >>> my_txt_new.rows
        3
        >>> my_txt_new.cols
        4
        '''

        # Creates a deep copy of the input nested list
        self.data = [row[:] for row in data]
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0


    def __str__(self):
        '''
        Returns a string describing the number of rows and columns
        Examples:
        >>> new_list = [[1,2,3,4],[4,5,6,7,8]]
        >>> my_txt_new = TxtData(new_list)
        >>> print(my_txt_new)
        This TxtData object has 2 rows and 4 columns.
        >>> list2 = [[7,8,6,4],[8,3,9,2,6],[3,5,0,1]]
        >>> my_txt_list2 = TxtData(list2)
        >>> print(my_txt_list2)
        This TxtData object has 3 rows and 4 columns.
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> print(my_txt)
        This TxtData object has 33 rows and 33 columns.  
        '''

        return "This TxtData object has " + str(self.rows) \
        + " rows and " + str(self.cols) + " columns."


    def get_pixels(self):
        '''
        Takes no explicit input and returns the total number of pixels in data
        Returns:
            (int): no of rows * no of columns
        Examples:
        >>> list2 = [[7,8,6,4],[8,3,9,2,6],[3,5,0,1]]
        >>> my_txt_list2 = TxtData(list2)
        >>> my_txt_list2.get_pixels()
        12
        >>> new_list = [[1,2,3,4],[4,5,6,7,8]]
        >>> my_txt_new = TxtData(new_list)
        >>> my_txt_new.get_pixels()
        8
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.get_pixels()
        1089 
        '''
        return self.rows * self.cols


    def get_data_at(self, row, col):
        '''
        Takes row and column indices as input and returns the value in data at that position.
        Parameters:
            row (int): Row index
            col (int): Column index
        Returns:
            (int): Value at the specified position in the data.
            ValueError: If the indices are out of bounds.
        Examples:
        >>> another_list = [5,4,3],[2,1,0]
        >>> my_txt_simple = TxtData(another_list)
        >>> my_txt_simple.get_data_at(0,0)
        5
        >>> new_list = [[1, 2, 3, 4], [4, 5, 6, 7, 8]]
        >>> my_txt_simple = TxtData(new_list)
        >>> my_txt_simple.get_data_at(1,0)
        4
        >>> list2 = [[7,8,6,4],[8,3,9,2,6],[3,5,0,1]]
        >>> my_txt_list2 = TxtData(list2)
        >>> my_txt_list2.get_data_at(2,3)
        1
        '''

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Index out of bound!")
        return self.data[row][col]


    def pretty_save(self, file_name):
        '''
        Converts data into a visually readable QR code and saves it to a file.
        '1's are converted into two block characters and '0's into two spaces.
        Parameters:
            file_name (str): Name of the file to save the new data.
        Returns:
            None (NoneType)
        Examples:
        >>> list2 = [[1, 0, 1], [0, 1, 0]]
        >>> my_txt_list2 = TxtData(list2)
        >>> my_txt_list2.pretty_save("qrcode_pretty.txt")
        # File "qrcode_pretty.txt" will contain: blocks ansd spaces
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("qrcode_pretty.txt")
        '''
        
        with open(file_name, 'w', encoding='utf-8') as f:
            for row in self.data:
                line = ""
                for val in row:
                    #Saving data as blocks and spaces
                    if val == 1:
                        line += BLOCK_CHAR 
                    else:
                        line += "  "  
                line += "\n" 
                f.write(line)


    def equals(self, another_data):
        '''
        Checks if the current TxtData object is equal to another TxtData object.
        Parameters:
            other (TxtData): The other TxtData object to compare with.
        Returns:
            (bool): True if the two TxtData objects are equal, False otherwise.
        Examples:
        >>> list2 = [[7, 8, 6, 4], [8, 3, 9, 2, 6]]
        >>> my_txt_list2 = TxtData(list2)
        >>> list3 = [[7, 8, 6, 4], [8, 3, 9, 2, 6]]
        >>> my_txt_list3 = TxtData(list3)
        >>> my_txt_list2.equals(my_txt_list3)
        True
        >>> another_list = [5,4,3],[2,1,0]
        >>> another_list_simple = TxtData(another_list)
        >>> another_list_simple2 = TxtData(another_list)
        >>> another_list_simple.equals(another_list_simple2)
        True
        >>> unequal_list = [6,7,9],[8,9,1]
        >>> other_unequal_list = [5,7,3],[4,9,0,2]
        >>> unequal_list_check = TxtData(unequal_list)
        >>> other_unequal_list_check = TxtData(other_unequal_list)
        >>> unequal_list_check.equals(other_unequal_list_check)
        False

        '''
        return self.data == another_data.data


    def approximately_equals(self, another_data, precision):
        '''
        Checks if two TxtData objects are approximately equal, considering a precision threshold.
        Parameters:
            another_data (TxtData): The other TxtData object to compare with.
            precision (float): The maximum allowed inconsistency rate.
        Returns:
            (bool): True if the two TxtData objects are approximately equal, False otherwise.
        Examples:
        >>> list2 = [[1, 0, 1], [0, 1, 0]]
        >>> my_txt_list2 = TxtData(list2)
        >>> list3 = [[1, 0, 1], [1, 0, 0]]
        >>> my_txt_list3 = TxtData(list3)
        >>> my_txt_list2.approximately_equals(my_txt_list3, 0.2)
        True
        >>> unequal_list = [6,7,9],[8,9,1]
        >>> other_unequal_list = [5,7,3],[4,9,0,2]
        >>> unequal_list_check = TxtData(unequal_list)
        >>> other_unequal_list_check = TxtData(other_unequal_list)
        >>> unequal_list_check.approximately_equals(other_unequal_list_check,0.5)
        False
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.approximately_equals(my_txt, 0.1)
        True
        '''
        # Checking if dimensions are different
        if self.rows != another_data.rows or self.cols != another_data.cols:
            return False 

        # Counting inconsistent values
        inconsistent_count = 0
        total_pixels = self.get_pixels()

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != another_data.data[i][j]:
                    inconsistent_count += 1

        # Calculating inconsistency rate
        inconsistency_rate = inconsistent_count / total_pixels
        return inconsistency_rate <= precision
