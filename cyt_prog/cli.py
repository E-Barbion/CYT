import sys
import shutil
from pathlib import Path

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
    print("SOURCE_NAME: " + SOURCE_NAME)
    print("SOURCE_PATH: " + SOURCE_PATH)
    print("OUTPUT_NAME: " + OUTPUT_NAME)
    print("OUTPUT_PATH: " + OUTPUT_PATH)

    out_dir = Path(OUTPUT_PATH) # OUTPUT_PATH = "cty_out/default/"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)