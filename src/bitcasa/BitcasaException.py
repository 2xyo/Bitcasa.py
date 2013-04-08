class BitCasaMaxConcurrentUpload(Exception):
    """Exception raised when we have reach the maximum of 3
    concurrent upload.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class BitCasaMaxConcurrentUpload(Exception):
    """Exception raised when we have reach the maximum of 3
    concurrent upload.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)