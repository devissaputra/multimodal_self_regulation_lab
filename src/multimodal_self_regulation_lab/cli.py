from __future__ import annotations
import runpy
from pathlib import Path

def main():
    demo=Path(__file__).resolve().parents[2]/"examples"/"demo.py"
    runpy.run_path(str(demo),run_name="__main__")

if __name__=="__main__": main()
