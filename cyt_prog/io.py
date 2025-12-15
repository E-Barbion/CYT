from pathlib import Path

def read_source(path):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    return text

def write_to_output(path, text):
    p = Path(OUTPUT_PATH)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return None