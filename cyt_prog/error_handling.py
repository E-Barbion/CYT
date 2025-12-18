import sys
from .cli import run_cli
from .diagnostics import *

def main() -> int:
    ctx = DiagnosticContext()

    try:
        run_cli(ctx)
        return 0
    except MissingInputFileError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    
    for w in ctx.warnings:
        print(format_warning(w), file=sys.stderr)