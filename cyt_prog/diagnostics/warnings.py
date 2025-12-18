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

class CYTRecoveryWarning(CYTWarning):
    """Warnings emitted upon sucessful error recovery."""

# User Warnings

class MissingOutputFileWarning(CYTUserWarning):
    """Warning caused by missing output file-path."""
    pass

class IllegalCharWarning(CYTRecoveryWarning):
    """Warning caused upon recovery of IllegalCharError"""
    pass