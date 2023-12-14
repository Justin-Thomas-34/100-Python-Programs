# Program 45: Python Program to Safely Create Nested Directory

# Solution: Using 3rd Variable

from pathlib import Path

Path("C:/Users/Desktop/new_dict/demo_dict").mkdir(parents=True,exist_ok=True)
