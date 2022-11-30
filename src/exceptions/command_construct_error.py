class InstructionConstructError(Exception):
    def __init__(self, err):
        msg = f"Error while constructing command after parsing, {err}"
        super().__init__(msg)
