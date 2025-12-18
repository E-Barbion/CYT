class CYTWarning:
    """Base class for all CYT warnings."""
    pass

# Main Warnings

class CYTUserWarning(CYTWarning):
    """Warnings caused by questionable but valid user input."""
    pass


class CYTStyleWarning(CYTWarning):
    """Warnings about style or non-idiomatic constructs."""
    pass

# User Warnings

class MissingOutputFileWarning(CYTUserWarning):
    """Warning caused by missing output file-path."""
    pass