class Node:
    def __init__(self, char): # Corrected: __init__
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end_of_word = False


class TernarySearchTree:
    def __init__(self): # Corrected: __init__
        self.root = None

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]

        if node is None:
            node = Node(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                node.is_end_of_word = True
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if not node:
            return False
        char = word[index]
        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index + 1 == len(word):
                return node.is_end_of_word
            return self._search(node.eq, word, index + 1)

# --- Test code from your original snippet (assuming insert_words.txt and corncob_lowercase.txt exist) ---

# Create TST and insert words
tst = TernarySearchTree()
words_to_insert = ["cat", "cap", "cape", "can", "dog", "dot", "dove", "apple"]

for word in words_to_insert:
    tst.insert(word)

print("Words inserted.")

##### Search for words
# Words that should be found
found_words = ["cat", "cap", "cape", "can", "dog", "dot", "dove", "apple"]

for word in found_words:
    result = tst.search(word)
    print(f"Search '{word}': {' Found' if result else ' Not Found'}")
tst.insert('abc')

# Load words from the insert_words.txt file and insert into the tree
# NOTE: This part assumes you have 'insert_words.txt' at the specified path.
# If not, this part will still cause a FileNotFoundError.
file_path_insert = r"/user/leuven/375/vsc37504/CPS/search_trees/insert_words.txt"

# Initialize TST (re-initializing for the file test)
tst = TernarySearchTree()

try:
    # Insert words from file
    with open(file_path_insert, 'r') as file:
        count = 0
        for line in file:
            word = line.strip()
            if word: # skip empty lines
                tst.insert(word)
                count += 1
    print(f"{count} words inserted into the Ternary Search Tree from '{file_path_insert}'.")

    # This block is redundant if the above correctly inserts unique words.
    # The set comprehension and re-insertion here would not change the TST
    # if the previous loop already inserted them. Keeping it for fidelity
    # to your original code, but noting its potential redundancy.
    with open(file_path_insert, 'r') as file:
        unique_words = set(word.strip() for word in file if word.strip())

    for word in unique_words:
        tst.insert(word)

    print(f"Total unique words inserted (after deduplication attempt): {len(unique_words)}")

except FileNotFoundError:
    print(f"Error: The file '{file_path_insert}' was not found. Skipping file insertion test.")
except Exception as e:
    print(f"An error occurred during file processing '{file_path_insert}': {e}")


# Sample words inserted
words_inserted = ["cat", "bat", "car", "can", "cap", "cape"]

# Insert into TST (re-initializing for this specific test block)
tst = TernarySearchTree()
for word in words_inserted:
    tst.insert(word)

# Check full words
print("\n🔍 Exact Match Tests:")
for word in words_inserted:
    print(f"Search '{word}': {'✅ Found' if tst.search(word) else '❌ Not Found'}")

# Now check that prefixes are not found
print("\n🔍 Prefix Match (should NOT be found):")
prefixes = ["ca", "ba", "cap", "c", "b", "baton", "catt"] # Note: "cap" is an exact word, it should be found

for prefix in prefixes:
    # Check if the prefix is an exact word in words_inserted
    if prefix in words_inserted:
        result = tst.search(prefix)
        print(f"Search '{prefix}' (exact word): {' Found' if result else ' Not Found'}")
    else:
        # For actual prefixes that are not full words
        result = tst.search(prefix)
        print(f"Search '{prefix}' (prefix/non-word): {' Not Found' if not result else ' Wrongly Found'}")


# Load words from the corncob_lowercase.txt file and insert into the tree
# NOTE: This part assumes you have 'corncob_lowercase.txt' at the specified path.
# If not, this part will still cause a FileNotFoundError.
file_path_corncob = r"/user/leuven/375/vsc37504/CPS/search_trees/corncob_lowercase.txt"

# Initialize TST (re-initializing for the final large file test)
tst = TernarySearchTree()

try:
    # Insert words from file
    with open(file_path_corncob, 'r') as file:
        count = 0
        for line in file:
            word = line.strip()
            if word: # skip empty lines
                tst.insert(word)
                count += 1
    print(f"\n{count} words inserted into the Ternary Search Tree from '{file_path_corncob}'.")
except FileNotFoundError:
    print(f"\nError: The file '{file_path_corncob}' was not found. Skipping large file insertion test.")
except Exception as e:
    print(f"\nAn error occurred during file processing '{file_corncob}': {e}")
