import os
import math
from collections import defaultdict
from openpyxl import Workbook

def calculate_entropy(file_path):
    byte_counts = defaultdict(int)

    with open(file_path, 'rb') as f:
        while (byte := f.read(1)):
            byte_counts[byte[0]] += 1 

    total_bytes = sum(byte_counts.values())

    entropy = 0.0
    for count in byte_counts.values():
        probability = count / total_bytes
        if probability > 0: 
            entropy -= probability * math.log2(probability) # энтропийка

    return byte_counts, total_bytes, entropy

def is_printable(byte_value):
    return 32 <= byte_value

def main():
    file_types = ['tif', 'jpg', 'gif', 'bmp']
    for file_type in file_types:
        file_path = f"tree.{file_type}" 
        if os.path.isfile(file_path):
            byte_counts, total_bytes, entropy = calculate_entropy(file_path)
            print(f"File: {file_path}")
            print(f"Total bytes: {total_bytes}")
            print("Byte counts:")
            for byte, count in sorted(byte_counts.items()):
                symbol = chr(byte) if is_printable(byte) else '.'
                print(f"Byte: {byte}, Symbol: '{symbol}', Count: {count}")
            print(f"Entropy: {entropy:.4f}\n")
        else:
            print(f"File {file_path} does not exist.\n")

if __name__ == "__main__":
    main()
