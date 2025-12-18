class CYTError(Exception):
    """Base class for all CYT-related errors."""
    pass

# Main Error Classes

class CYTUserError(CYTError):
    """Errors caused by invalid user input or usage."""
    pass


class CYTInternalError(CYTError):
    """Errors indicating a bug or violated invariant."""
    pass


class CYTEnvironmentError(CYTError):
    """Errors caused by external systems."""
    pass

# User Errors

class MissingInputFileError(CYTUserError):
    """No input file was provided to the CLI."""
    pass


# Internal Errors


# Environmental Errors