#!/usr/bin/env python3
"""
Basic usage examples for csv-stringify package.
"""

from csv_stringify import stringify

def main():
    print("=== CSV Stringify Examples ===\n")
    
    # Example 1: Basic usage (matching Node.js)
    print("1. Basic Usage (Node.js equivalent):")
    output = stringify([
        ["1", "2", "3", "4"],
        ["a", "b", "c", "d"],
    ], header=False)
    
    print("Output:", repr(output))
    print("CSV:")
    print(output)
    
    # Example 2: Simple data without headers
    print("2. Simple Data:")
    data = [["1", "2", "3"], ["a", "b", "c"]]
    csv_string = stringify(data, header=False)
    print("Input:", data)
    print("Output:", repr(csv_string))
    print("CSV:")
    print(csv_string)
    
    # Example 3: With headers
    print("3. With Headers:")
    csv_string = stringify(data, columns=["A", "B", "C"])
    print("Output:", repr(csv_string))
    print("CSV:")
    print(csv_string)
    
    # Example 4: From dictionaries
    print("4. From Dictionaries:")
    data = [{"name": "John", "age": 25}]
    csv_string = stringify(data)
    print("Input:", data)
    print("Output:", repr(csv_string))
    print("CSV:")
    print(csv_string)

if __name__ == "__main__":
    main()