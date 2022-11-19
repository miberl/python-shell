# Provided option flag could not be recognised
class UnknownFlagError(Exception):
    def __init__(self, option_flag_error):
        message = f"Unknown option flag: {option_flag_error}"
        super().__init__(message)