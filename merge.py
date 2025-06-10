#!/usr/bin/env python3

import os
import shutil
from pathlib import Path

def merge_folders():
    source_dir = Path("RealMadrid_remaining")
    target_dir = Path("data")
    
    if not source_dir.exists():
        print(f"Source directory {source_dir} does not exist")
        return
    
    if not target_dir.exists():
        print(f"Target directory {target_dir} does not exist")
        return
    
    for item in source_dir.iterdir():
        if item.is_file():
            target_file = target_dir / item.name
            if target_file.exists():
                print(f"Overwriting {target_file}")
            shutil.copy2(item, target_file)
            print(f"Copied {item} -> {target_file}")
        
        elif item.is_dir():
            target_subdir = target_dir / item.name
            target_subdir.mkdir(exist_ok=True)
            
            for subitem in item.iterdir():
                target_subfile = target_subdir / subitem.name
                if target_subfile.exists():
                    print(f"Overwriting {target_subfile}")
                shutil.copy2(subitem, target_subfile)
                print(f"Copied {subitem} -> {target_subfile}")
    
    print(f"\nMerge complete")

if __name__ == "__main__":
    merge_folders() 