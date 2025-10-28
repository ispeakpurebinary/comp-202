from helper import convert_date, get_data
from txtdata import TxtData

#Constants
DEFAULT_UPDATE_DATE = "00/00/0000"
DEFAULT_OWNER = "Default Owner"
DEFAULT_ERROR_CORRECTION = 0.0

class QRCode:
    '''
    Provides methods for comparing QR codes, checking corruption, and representing QR code details.
    Instance Attributes:
        data (TxtData): A TxtData object containing the binary data for the QR code.
        last_update_date (dict): A dictionary representing the last update date with keys 'Day', 'Month', and 'Year'.
        owner (str): The name of the QR code's owner.
        error_correction (float): The error correction level of the QR code (range: 0.0 to 1.0).
    '''

    def __init__(self, file_path, last_update_date= DEFAULT_UPDATE_DATE, owner= DEFAULT_OWNER,\
                error_correction= DEFAULT_ERROR_CORRECTION):
        """
        Initializes a QRCode object 
        Parameters:
            file_path (str): Path to the binary file containing the QR code data.
            last_update_date (str): The last update date of the QR code in DD/MM/YYYY format.
            owner (str): Name of the QR code's owner. Defaults to "Default Owner".
            error_correction (float): The error correction level (range: 0.0 to 1.0). Defaults to 0.0.
        Returns:
            None
        Examples:
        >>> qrcode1 = QRCode("qrcode_binary.txt", "15/07/2024", "Alice", 0.1)
        >>> print(qrcode1.last_update_date['Day'])
        '15'
        >>> print(qrcode1.last_update_date['Month'])
        '07'
        >>> print(qrcode1.last_update_date['Year'])
        '2024'
        >>> my_qrcode.owner
        'Alice'
        >>> my_qrcode.error_correction
        0.1
        >>> qrcode2 = QRCode("qrcode_binary_copy.txt", "12/06/2023", "Bob", 0.2)
        >>> print(qrcode2.last_update_date['Day'])
        12
        >>> print(qrcode2.last_update_date['Month'])
        06
        >>> print(qrcode2.last_update_date['Year'])
        2023
        >>> qrcode2.owner
        'Bob'
        >>>qrcode2.error_correction
        0.2
        >>> qrcode3 = QRCode("qrcode_corrupted.txt", "25/12/2022", "Sara", 0.15)
        >>> print(qrcode3.last_update_date['Day'])
        25
        >>> print(qrcode3.last_update_date['Month'])
        12
        >>> print(qrcode3.last_update_date['Year'])
        2022
        >>> qrcode3.owner
        'Sara'
        >>>qrcode3.error_correction
        0.15
        """

        # Creates a TxtData object from the file
        self.data = TxtData(get_data(file_path)) 
        self.last_update_date = convert_date(last_update_date)  
        self.owner = owner
        self.error_correction = error_correction


    def __str__(self):
        """
        Returns a string describing the QRCode object, including owner, last update year, and data dimensions.
        Returns:
            (str): A description of the QR code.
        Examples:
        >>> qrcode1 = QRCode("qrcode_binary.txt", "15/07/2024", "Alice", 0.1)
        >>> print(qrcode1)
        The QR code was created by Alice and last updated in 2024.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        >>> qrcode2 = QRCode("qrcode_binary_copy.txt", "12/06/2023", "Bob", 0.2)
        >>> print(qrcode2)
        The QR code was created by Bob and last updated in 2023.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        >>> qrcode3 = QRCode("qrcode_corrupted.txt", "25/12/2022", "Carol", 0.15)
        >>> print(qrcode3)
        The QR code was created by Sara and last updated in 2022.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        """

        return (
            f"The QR code was created by {self.owner} and last updated in {self.last_update_date['Year']}.\n"
            f"The details regarding the QR code file are as follows:\n"
            f"{self.data}")


    def equals(self, another_qrcode):
        """
        Checks if the current QRCode object is equal to another QRCode object.
        Parameters:
            another_qrcode (QRCode): The other QRCode object to compare with.
        Returns:
            (bool): True if the QRCode objects are equal, False otherwise.
        Examples:
        >>> qrcode1 = QRCode("qrcode_binary.txt", "01/09/2024", "Alice", 0.1)
        >>> qrcode2 = QRCode("qrcode_binary_copy.txt", "01/09/2024", "Alice", 0.1)
        >>> qrcode1.equals(qrcode2)
        True
        >>> qrcode3 = QRCode("qrcode_corrupted.txt", "25/12/2022", "Carol", 0.15)
        >>> qrcode1.equals(qrcode3)
        False
        >>> qrcode4 = QRCode("qrcode_binary.txt", "01/09/2024", "Alice", 0.2)
        >>> qrcode1.equals(qrcode4)
        False
        """
        return self.data.equals(another_qrcode.data) and \
               self.error_correction == another_qrcode.error_correction


    def is_corrupted(self, precise_qrcode):
        """
        Checks if the QRCode object is corrupted by comparing it with a precise QRCode object.
        Parameters:
            precise_qrcode (QRCode): A QRCode object representing the precise version of the QR code.
        Returns:
            (bool): True if the QRCode is corrupted, False otherwise.
        Raises:
            ValueError: If the dimensions of the two QR codes do not match.
        Examples:
        >>> precise_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Alice", 0.1)
        >>> corrupted_qrcode = QRCode("qrcode_corrupted.txt", "25/12/2022", "Carol", 0.15)
        >>> precise_qrcode.is_corrupted(corrupted_qrcode)
        False
        >>> corrupted_qrcode.data.data[0][0] = 1
        >>> precise_qrcode.is_corrupted(corrupted_qrcode)
        True
        >>> precise_qrcode2 = QRCode("qrcode_binary_copy.txt", "01/09/2024", "Alice", 0.1)
        >>> precise_qrcode.is_corrupted(precise_qrcode2)
        False
        """

        return not self.data.approximately_equals(precise_qrcode.data, self.error_correction)
