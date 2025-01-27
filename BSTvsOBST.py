from requests_html import HTMLSession  # Importing HTMLSession from requests_html to scrape webpage content
from wordcloud import WordCloud, STOPWORDS  # Importing WordCloud for generating word clouds and STOPWORDS for excluding common words
import matplotlib.pyplot as plt  # Importing matplotlib for visualizing the word cloud
import matplotlib.colors as mcolors  # Importing mcolors for defining custom colormap
import random  # Importing random for shuffling word list

# Define a custom colormap for the word cloud visualization
# Colors are chosen to match a custom palette that will be applied to the word cloud
custom_cmap = mcolors.ListedColormap(['#E06C4E', '#E64D4D', '#E8B88C', '#499B8A', '#318887'])

# Function to compute the cost of the Optimal Binary Search Tree (OBST)
# Uses dynamic programming to calculate the minimum cost of searching in an optimal BST
# Reference: https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
def optimal_bst(freq, n):
    # Initialize a 2D list to store the cost of optimal BSTs for subarrays
    cost = [[0 for x in range(n)] for y in range(n)]
    sum_freq = [0] * n  # List to store the cumulative frequency sum for efficient calculation
    
    # Calculate cumulative frequencies
    sum_freq[0] = freq[0]
    for i in range(1, n):
        sum_freq[i] = sum_freq[i-1] + freq[i]
    
    # Dynamic programming approach to calculate the minimum cost for every subarray of frequencies
    for length in range(1, n+1):  # Iterate over all subarrays of increasing length
        for i in range(n - length + 1):  # Iterate over all possible starting points of the subarray
            j = i + length - 1  # Determine the end point of the subarray
            if length == 1:
                cost[i][j] = freq[i]  # Cost of a single node is just its frequency
            else:
                cost[i][j] = float('inf')  # Initialize the cost as infinity for comparison
                for r in range(i, j+1):  # Iterate over all possible root nodes in the range
                    left_cost = cost[i][r-1] if r > i else 0  # Cost of the left subtree
                    right_cost = cost[r+1][j] if r < j else 0  # Cost of the right subtree
                    # Calculate the cost of choosing r as root
                    cost[i][j] = min(cost[i][j], left_cost + right_cost + sum_freq[j] - (sum_freq[i-1] if i > 0 else 0))
    
    # Return the minimum cost of the OBST for the entire range
    return cost[0][n-1]

# Function to build a regular Binary Search Tree (BST) and compute its traversal cost
# It calculates the cost of accessing all nodes in the BST in an ordered fashion
def regular_bst_cost(words, frequencies):
    cost = 0  # Initialize traversal cost
    words_sorted = sorted(zip(words, frequencies), key=lambda x: x[0])  # Sort words alphabetically
    level = 1  # Starting level of the tree (root node)
    
    # For each word, calculate its contribution to the cost based on its level in the tree
    for word, freq in words_sorted:
        cost += level * freq  # Multiply frequency by the level (depth) of the node
        level += 1  # Increment the level for the next word in the sorted list
    return cost

# Function to scrape webpage content and generate a word cloud
def get_word_cloud_from_webpage(url):
    session = HTMLSession()  # Create a new session to handle the HTTP request
    response = session.get(url)  # Send GET request to the specified URL
    article_text = ' '.join(p.text for p in response.html.find('p'))  # Extract all text inside <p> tags
    
    stopwords = set(STOPWORDS)  # Get the set of stopwords to exclude common words from the word cloud
    
    # Generate a word cloud using the extracted article text
    wordcloud = WordCloud(
        width=1000,  # Width of the word cloud image
        height=500,  # Height of the word cloud image
        background_color='#071932',  # Background color of the word cloud
        stopwords=stopwords,  # Exclude stopwords from the word cloud
        collocations=False,  # Disable the default behavior of combining two-word phrases
        min_font_size=10,  # Set the minimum font size for the words
    ).generate(article_text)  # Generate word cloud from the article text
    
    word_frequencies = wordcloud.words_  # Get the word frequencies (word-cloud generated data)
    return word_frequencies  # Return the frequencies for further analysis

# Function to simulate the comparison between a regular BST and OBST
def compare_trees(word_cloud):
    # Sort the word frequencies in descending order and select the top 50
    sorted_word_freq = sorted(word_cloud.items(), key=lambda x: x[1], reverse=True)
    top_words = [word for word, _ in sorted_word_freq[:50]]  # Get the top 50 words
    frequencies = [freq for _, freq in sorted_word_freq[:50]]  # Get the frequencies of those words
    
    # Shuffle the word list to simulate randomness in the tree structure
    random.shuffle(top_words)
    
    # Calculate the traversal cost of the regular BST
    bst_cost = regular_bst_cost(top_words, frequencies)
    
    # Calculate the traversal cost of the optimal BST (OBST)
    obst_cost = optimal_bst(frequencies, len(frequencies))
    
    # Return the costs of both trees for comparison
    return bst_cost, obst_cost

# Main function to execute the workflow
def main():
    # URL of the webpage to scrape and analyze
    url = 'https://gkids.com/ghiblifest/'  # Example URL for testing

    # Get the word frequencies from the webpage
    word_cloud = get_word_cloud_from_webpage(url)

    # Compare the traversal costs of the regular BST and the OBST
    bst_cost, obst_cost = compare_trees(word_cloud)

    # Print the results of the comparison
    print(f"Regular BST traversal cost: {bst_cost:.2f}")
    print(f"Optimal BST traversal cost: {obst_cost:.2f}")

    # Visualize the word cloud with the defined custom colormap and background color
    wordcloud = WordCloud(width=1000, height=500, background_color='#071932', colormap=custom_cmap).generate_from_frequencies(word_cloud)

    # Set the background color of the plot to match the word cloud's background
    plt.gca().set_facecolor('#071932')

    # Display the word cloud in a figure
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")  # Hide the axes for a clean view
    plt.tight_layout(pad=0)  # Adjust layout for no padding
    plt.show()  # Show the generated word cloud

# Run the main function
if __name__ == '__main__':
    main()  # Call the main function to execute the code
