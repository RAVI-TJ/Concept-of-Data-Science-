# 🔍 Ternary Search Tree (TST) – HPC-Based Data Science Project (2024–2025)

## 🎓 Master's Project – Concepts of Data Science  
**Student 1:** Nuthi Raviteja Pediredla  [2468496]
**Student 2:** Laiba Tahir [2469634] 
**Course:** Concepts of Data Science  
**University:** Hasselt University  
**Cluster Used:** Genius (VSC HPC)

---

## 📘 Overview

This project focuses on implementing a **Ternary Search Tree (TST)** for efficient string storage and lookup. The TST combines the performance advantages of tries with the space efficiency of binary search trees. The main objectives are to:

- Verify correctness using unit tests
- Insert and search large datasets (~58k words)
- Ensure prefix-only queries are rejected
- Benchmark performance on HPC with SLURM
- Plot insert/search time as dataset size increases

---

## 🛠️ Project Workflow

1. **TST Implementation**
   - Developed `Node` and `TernarySearchTree` classes
   - Implemented `insert()`, `search()`, and `get_all_words()`
2. **Local Testing**
   - Inserted sample words: `"cat", "cape", "can", "dog", "dot"`
   - Verified:
     - Exact matches succeed ✅
     - Prefixes return false ❌
     - Empty strings are ignored
     - Duplicates are handled
3. **Dataset Integration**
   - Used `corncob_lowercase.txt` (58,110 English words)
   - Confirmed all words were inserted and retrieved
4. **Negative Case Testing**
   - Used `not_insert_words.txt` to ensure no false matches
5. **GitHub Version Control**
   - Utilized branches and resolved merge conflicts
   - Pushed `.ipynb`, `.py`, benchmark, and SLURM script files
6. **HPC Execution via SLURM**
   - Created and activated a virtual environment in the script
   - Converted `.ipynb` to `.py`
   - Submitted the job using:
     ```bash
     sbatch -M genius tst_terenary.slurm
     ```
7. **Benchmarking**
   - Measured insert/search times for increasing word counts (step = 1000)
   - Plotted results using `matplotlib`
8. **Time Complexity Analysis**
   - Compared actual and theoretical complexity
   - Observed nearly linear scaling for insert and search

---

## 📊 Time Complexity of TST Operations

### 🔹 `insert(word)`
- Time complexity: **O(L × log N)**
- Each character descends one level (L = word length)
- Binary search logic at each node → log N comparisons

### 🔹 `search(word)`
- Time complexity: **O(L × log N)**
- Follows the same path as `insert()`, without mutation

### 🔹 Space complexity
- **O(N × L)** in the worst case
  - N = number of unique words
  - L = average word length
- More compact than a trie; each node stores one character with three child links (left, middle, right)

---

## 📈 Performance Graph

- Benchmarked insert and search for 1,000 to 58,000 words
- Timed operations using `time.time()`
- Results show near-linear scaling for both operations
- Graph details:
  - X-axis: number of words
  - Y-axis: time (seconds)
  - Blue: Insert
  - Green: Search

---

## 📁 Repository Structure
```
.
├── ternary_search_tree.py           # Core TST implementation
├── benchmark_tst.py                # Benchmarking insert/search
├── tst_terenary.slurm              # SLURM HPC script
├── ternary-search-tree-project.ipynb # Notebook for development/testing
├── ternary_test.out                # Output log from HPC job
├── requirements.txt                # Dependencies
└── search_trees/
    ├── corncob_lowercase.txt       # 58,110 English words
    └── not_insert_words.txt        # Negative test dataset
```

---

## 🖥️ SLURM Job Script (`tst_terenary.slurm`)

```bash
#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --partition=genius
#SBATCH --job-name=ternary_test
#SBATCH --output=ternary_test.out
#SBATCH --time=00:10:00
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --account=lp_h_ds_students

source ~/venv/bin/activate
/usr/bin/time -p python3 benchmark_tst.py
```

**📦 Requirements**

- `matplotlib`
- Install dependencies with:
  ```
  pip install -r requirements.txt
  ```

---

## ✅ Conclusion

This project demonstrates the implementation, testing, and benchmarking of a Ternary Search Tree (TST) on both small and large datasets using Python and the VSC Genius HPC cluster.

**Key takeaways:**

- Correct handling of insertions, searches, and negative cases
- Scalability shown through performance graphs
- Practical SLURM job submission and resource management on HPC
- Strong understanding of data structure design and complexity analysis

This experience enhanced our skills in algorithmic thinking, benchmarking, and applying HPC in data science.
