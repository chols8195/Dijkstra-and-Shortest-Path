from heapq import heappush, heappop, heapify
from collections import defaultdict
import math
import os
from bitarray import bitarray

# Function to generate Huffman codes based on character frequencies
# Referenced module 18 slide 63
def huffmanCode(freq_dict):
    """Generate Huffman codes for the given frequency dictionary."""
    # Create a heap with initial frequencies and empty codes
    heap = [[freq, [char, ""]] for char, freq in freq_dict.items()]
    heapify(heap)  # Turn the list into a min-heap

    # Combine the two smallest nodes iteratively to build the Huffman Tree
    while len(heap) > 1:
        lo = heappop(heap)  # Pop the smallest node
        hi = heappop(heap)  # Pop the next smallest node

        # Assign "0" to the left branch and "1" to the right branch
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        # Push the combined node back into the heap
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Convert the result into a dictionary for easy look-up
    return {char: code for char, code in heappop(heap)[1:]}

# Function to analyze a text file and calculate Huffman codes
def huffmanTable():
    """Analyze a text file, calculate Huffman codes, and display efficiency metrics."""
    file = input("Enter a file name to encode: ").strip()

    # Check if the file exists
    if not os.path.isfile(file):
        print("File does not exist.")
        return None, None, None

    # Read the file content
    with open(file, 'r') as inputFile:
        text = inputFile.read()

    # Total number of bits in ASCII encoding
    totalBits = len(text) * 8

    # Calculate character frequencies
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    # Generate the Huffman codes
    huffTree = huffmanCode(freq_dict)

    # Display the Huffman table
    print("-------------------------------------------------------------------------------")
    print(f"Character\t\tWeight\t\tHuffman Code")
    print("-------------------------------------------------------------------------------")
    huffCost = 0  # Track the cost of encoding using Huffman codes
    for char, code in huffTree.items():
        huffCost += len(code) * freq_dict[char]  # Calculate the cost for each character
        displayChar = char if char not in {" ", "\n"} else repr(char)
        print(f'{displayChar}\t\t\t\t{freq_dict[char]}\t\t\t{code}')
        
    print("-------------------------------------------------------------------------------")
    print("Results:")
    print("-------------------------------------------------------------------------------")
    
    print(f"Expected cost of Huffman code: {huffCost}")
    asciiCost = totalBits
    print(f"Expected cost of ASCII: {asciiCost}")

    # Calculate Huffman efficiency improvement over ASCII
    efficiencyImprovement = 100 - (100 * (huffCost / asciiCost))
    print(f"Huffman efficiency improvement over ASCII code: {efficiencyImprovement:.2f}%")

    # Calculate the Fixed-Length Code (FCL) cost
    FCLCost = len(text) * math.ceil(math.log2(len(freq_dict)))
    print(f"Expected cost of optimal FCL cost: {FCLCost}")

    # Calculate Huffman efficiency improvement over FCL
    FCLImprovement = 100 - (100 * (huffCost / FCLCost))
    print(f"Huffman efficiency improvement over FCL: {FCLImprovement:.2f}%")

    return huffTree, len(text), os.path.splitext(file)[0]

# Function to compress a file using Huffman encoding
def zip(input_file, output_file, huffman):
    """Compress a text file using Huffman encoding."""
    # Read the input file
    with open(input_file, "r") as file:
        text = file.read()

    # Create a bitarray for encoded text
    encoded_bits = bitarray()
    # Encode the text using the Huffman codes
    for char in text:
        encoded_bits.extend(bitarray(huffman[char]))  # Extend the bitarray with Huffman codes

    # Write the compressed data to the output file
    with open(output_file, "wb") as output:
        encoded_bits.tofile(output)  # Save the bitarray to the file

    # Display file size statistics
    print(f"The size of {input_file}: {os.stat(input_file).st_size} bytes")
    print(f"The size of {output_file}: {os.stat(output_file).st_size} bytes")


# Function to decompress a Huffman-encoded file
def unzip(zip_file, huffman, text_length):
    """Decompress a Huffman-encoded file."""
    # Read the compressed file
    with open(zip_file, "rb") as file:
        encoded_bits = bitarray()
        encoded_bits.fromfile(file)  # Load the bitarray from the file

    # Reverse the Huffman map for decoding
    reverse_huffman = {code: char for char, code in huffman.items()}

    # Decode the bitarray back into the original text
    decoded_text = []
    code = ""
    for bit in encoded_bits:
        code += '1' if bit else '0'
        if code in reverse_huffman:  # If a complete code is found
            decoded_text.append(reverse_huffman[code])  # Add the corresponding character
            code = ""  # Reset the code for the next character

    # Write the decompressed text to a new file
    output_file = f"{os.path.splitext(zip_file)[0]}.unzipped.txt"
    with open(output_file, "w") as file:
        file.write("".join(decoded_text))  # Save the decoded text to a file

    # Display the size of the decompressed file
    print(f"The size of {output_file}: {os.stat(output_file).st_size} bytes")

# Main function to run the Huffman encoding program
def main():
    """Main function to handle file compression and decompression."""
    # Generate Huffman codes and analyze the file
    huffmanMap, text_length, file_base = huffmanTable()
    if not huffmanMap:
        return  # If no Huffman map is returned, terminate

    # Define input and output file names
    input_file = f"{file_base}.txt"
    zip_file = f"{file_base}.zip"

    # Compress the input file
    zip(input_file, zip_file, huffmanMap)

    # Decompress the compressed file
    unzip(zip_file, huffmanMap, text_length)

# Entry point of the script
if __name__ == "__main__":
    main()
