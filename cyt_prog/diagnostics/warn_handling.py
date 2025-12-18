from typing import List
from .warnings import *

class DiagnosticContext:
    def __init__(self):
        self.warnings: List[CYTWarning] = []

    def warn(self, warning: CYTWarning) -> None:
        self.warnings.append(warning)


def format_warning(w: CYTWarning) -> str:
    if isinstance(w, MissingOutputFileWarning):
        return f"Warning: No output directory given. Output will be at {OUTPUT_PATH}"
    return "Warning"