import os
import math
from collections import defaultdict

def calculate_entropy_incremental(byte_counts, total_bytes):
    entropy = 0.0
    for count in byte_counts.values():
        probability = count / total_bytes
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

def is_printable(byte_value):
    return 32 <= byte_value

def main():
    file_types = ['tif', 'jpg', 'gif', 'bmp']
    for file_type in file_types:
        file_path = f"tree.{file_type}"
        if os.path.isfile(file_path):
            byte_counts = defaultdict(int)
            total_bytes = 0
            
            print(f"File: {file_path}")
            print("Byte counts and entropy change:")

            with open(file_path, 'rb') as f:
                while (byte := f.read(1)):
                    byte_value = byte[0]
                    byte_counts[byte_value] += 1  
                    total_bytes += 1

                    current_entropy = calculate_entropy_incremental(byte_counts, total_bytes)

                    symbol = chr(byte_value) if is_printable(byte_value) else '.'
                    print(f"Byte: {byte_value}, Symbol: '{symbol}', Count: {byte_counts[byte_value]}, Current Entropy: {current_entropy:.4f}")
            
            print(f"\nFinal entropy for {file_path}: {current_entropy:.4f}\n")
        else:
            print(f"File {file_path} does not exist.\n")

if __name__ == "__main__":
    main()
