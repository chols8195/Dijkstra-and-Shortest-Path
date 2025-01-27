----
*  **Name      :**  Lisa Cho        
*  **Student ID:**  110795430            
*  **Class     :**  CSCI 3412 Section 02           
*  **PA#       :**  6               
*  **Due Date  :**  November 14, 2024
----

# Read Me
## Homework Overview

## Requirements

- Python 3
- `King.txt` file or any text file

## Table of Contents

- [Homework Structure](#homework-structure)
- [Algorithms and Approach](#algorithms-and-approach)
  - [Q1) Dijkstra's Algorithm](#dijkstra-algorithm)
  - [Q2) Dijkstra's SSSP and MST algorithms](#dijkstra-SSSP-and-MST-algorithms)
  - [Q3) TinyZip and TinyUnzip](#tinyzip-and-tinyunzip)
- [Execution](#execution)
- [Extra Credit](#extra-credit)

## Homework Structure


## Algorithms and Approach

### Dijkstra Algorithm

## Source file
***Dijkstra.py***

1. **Purpose**: 
   - This program implements Dijkstra's algorithm to compute the shortest paths from a start node to all other nodes in a directed weighted graph.
2. **Implementation**: 
   - **Graph Class**: Manages nodes, edges, and edge weights.
   - **dijkstra Function**: Calculates shortest paths and prints relaxation steps.
   - **Output**: Displays the history of relaxed edges, visited nodes, and final shortest distances.
3. **Output**:
   - Nodes added to visited list with their weights.
   - Relaxation steps (edge updates).
   - Final shortest distances and paths.
4. **Source References**:
   - Implementation based on standard Dijkstra's algorithm and online sources.

### Dijkstra SSSP and MST algorithms

## Source file
***ShortestDistanceCity.py***

1. **Purpose**: 
   - The task involves creating a program to help users plan trips in the United States by determining the shortest distances between cities and finding the Minimum Spanning Tree (MST) of the cities. We will use Dijkstra’s Shortest Path First (SSSP) algorithm to find the shortest paths from a starting city to all other cities, and Prim's algorithm will be used to find the MST. The program will use a distance table between 15 cities.
2. **Implementation**: 
    ***Graph Class:***
   - The class will represent the cities and their distances.
   - It will include methods for Dijkstra’s and Prim’s algorithms.
   
    ***Dijkstra’s Algorithm:***
   - The method will take a source city and find the shortest path to all other cities using a priority queue.
   
    ***Prim’s MST Algorithm:***
   - The method will start with a city and connect the cities using the minimum edge weight at each step.
3. **Output**:
   - The output of this code will display the shortest distances from a specified city (e.g., Dallas) to all other cities in the distance table using Dijkstra's algorithm, and it will also compute the Minimum Spanning Tree (MST) for the network of cities using Prim's algorithm. The results will show the shortest paths for each city and the total distance of the MST connecting all cities with the minimum total edge weight.

### TinyZip and Unzip

## Source file
***TinyUnzip.py***

1. **Purpose**: 
   - implement Huffman coding for compressing and decompressing text files, providing an efficient way to reduce file size based on character frequency.
2. **Implementation**: 
   - functions to generate Huffman codes, compress files using those codes, and decompress the binary file back to its original form.
3. **Output**:
   - functions to generate Huffman codes, compress files using those codes, and decompress the binary file back to its original form.
---

## Execution
To run the program, follow these steps:

1. **Prepare Data**: 
   - Ensure that the `King.txt` file (or any text file you wish to use for Huffman coding and compression) is placed in the same directory as your Python scripts.
   - For the Dijkstra and MST parts, you will need a graph of cities and distances, which should be hardcoded or provided in a format compatible with your `ShortestDistanceCity.py` script.

2. **Run the Script**:
   - **For Dijkstra Algorithm**: Execute the `Dijkstra.py` script to find the shortest paths in the graph. This script will calculate the shortest distances from a given start node to all other nodes in a weighted graph.
     ```bash
     python Dijkstra.py
     ```
   - **For Shortest Distance City and MST**: Run the `ShortestDistanceCity.py` script. This will use Dijkstra's algorithm to find the shortest distances between cities and Prim's algorithm to compute the Minimum Spanning Tree (MST) based on a distance table.
     ```bash
     python ShortestDistanceCity.py
     ```
   - **For TinyZip and TinyUnzip**: To compress and decompress files, run the `TinyUnzip.py` script, which implements Huffman coding for efficient file compression.
     ```bash
     python TinyUnzip.py
     ```

3. **View Results**: 
   - For **Dijkstra Algorithm**, the output will display the relaxation steps, visited nodes with weights, and the final shortest distances from the start node to all other nodes.
   - For **Shortest Distance City and MST**, the output will display the shortest path distances from the source city (e.g., Dallas) to other cities and the Minimum Spanning Tree (MST) of all cities.
   - For **TinyZip and TinyUnzip**, the output will show the compression and decompression results, including the compressed binary file and the original text after decompression.

4. **Extra Credit**: 
   - **Word Cloud and OBST**: If you are completing the extra credit, run the `BSTvsOBST.py` script, which will scrape a webpage for text, create a word cloud, and calculate traversal costs for both a regular Binary Search Tree (BST) and an Optimal Binary Search Tree (OBST) based on word frequencies.
     ```bash
     python BSTvsOBST.py
     ```

5. **Requirements**: 
   - Ensure that you have Python 3 installed, along with any necessary dependencies for running the scripts (e.g., libraries for Huffman coding, Dijkstra's algorithm, or web scraping). You may need to install libraries like `heapq` (for priority queues) or `wordcloud` (for generating word clouds).
   - Example of installing required libraries:
     ```bash
     pip install heapq wordcloud

To run the program, follow these steps:

1. **Prepare Data**: Place `King.txt` in the project directory (or any text file you wish to use).
2. **Run the Script**: Execute the script in VS Code or a terminal:
   ```bash
   python main.py


# Extra Credit

## EC: Word Cloud and OBST


## Source file
***BSTvsOBST.py***

1. **Purpose**: 
   -  The purpose of this code is to scrape content from a webpage, generate a word cloud from the text, and compare the traversal costs of a regular Binary Search Tree (BST) with an Optimal Binary Search Tree (OBST), based on word frequency data.
2. **Implementation**: 
   - The implementation includes functions to scrape webpage content, create a word cloud, calculate the cost of traversing a regular BST and an OBST, and visualize the word cloud using a custom colormap.
3. **Output**
   - The output includes the traversal costs of both the regular BST and the OBST, displayed as numerical values, along with a visual word cloud of the most frequent words from the webpage.
