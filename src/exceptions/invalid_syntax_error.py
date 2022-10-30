class InvalidSyntaxError(Exception):
    def __init__(self, parser_error):
        message = f"Invalid syntax, see '{parser_error}', stopping!"
        super().__init__(message)
