class InstructionConstructError(Exception):
    def __init__(self, construct_error):
        message = f"Error while constructing command after parsing, {construct_error}"
        super().__init__(message)
