import sys
import shutil
from pathlib import Path
import cyt_prog.frontend.parser as parser
import cyt_prog.io as io

def main():
    if len(sys.argv) > 1:
        dirs1 = sys.argv[1].split("/")
        SOURCE_NAME = dirs1[len(dirs1)-1].strip(".py")
        SOURCE_PATH = sys.argv[1]
        if len(sys.argv) > 2:
            dirs2 = sys.argv[2].split("/")
            OUTPUT_NAME = dirs2[len(dirs2)-1]
            OUTPUT_PATH = "cyt_out/" + OUTPUT_NAME
        else:
            OUTPUT_NAME = "default"
            OUTPUT_PATH = "cyt_out/default/"
            print("Note : No output directory given. Output will be at " + OUTPUT_PATH)
    else: sys.exit(print("Error: no file given! exiting..."))
    print("debug1 : results of I/O parsing...")
    print("SOURCE_NAME: " + SOURCE_NAME)
    print("SOURCE_PATH: " + SOURCE_PATH)
    print("OUTPUT_NAME: " + OUTPUT_NAME)
    print("OUTPUT_PATH: " + OUTPUT_PATH)

    # Invariant:
    # - cyt_out/<OUTPUT_NAME>/ is deleted and recreated at program start
    # - After initialization, the directory exists and is empty
    # - No existence checks are required for files inside it
    out_dir = Path(OUTPUT_PATH)
    ast = out_dir / "ast.txt"
    ri = out_dir / "ir.txt"
    c = out_dir / f"{OUTPUT_NAME}.c"
    build = out_dir / "build.log"
    runtime = out_dir / "runtime/"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    ast.touch()
    ri.touch()
    c.touch()
    build.touch()
    runtime.mkdir()
    print("debug1 : created files / directories...")
    for entry in out_dir.iterdir():
        print(entry)
    

    source_text = io.read_source(SOURCE_PATH)
    parsed_source = parser.parse(source_text)
    io.write_to_output(OUTPUT_PATH + "/ast.txt", source_text)