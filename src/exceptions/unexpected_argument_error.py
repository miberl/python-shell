# Exception raised when options don't match format
class UnexpectedArgumentError(Exception):
    def __init__(self, unexpected_args_error):
        message = f"Unexpected argument: {unexpected_args_error}"
        super().__init__(message)
