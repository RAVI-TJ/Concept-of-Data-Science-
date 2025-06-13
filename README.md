# 🔍 Ternary Search Tree (TST) – HPC-Based Data Science Project (2024–2025)

## 🎓 Master's Project – Concepts of Data Science  
**Student 1:** Nuthi Raviteja Pediredla  
**Student 2:** [Teammate Name Here]  
**Course:** Concepts of Data Science  
**University:** Hasselt University  
**Cluster Used:** Genius (VSC HPC)

---

## 📘 Overview

This project implements a **Ternary Search Tree (TST)** for efficient storage and lookup of strings. The TST balances the performance benefits of tries with the space efficiency of binary search trees. The aim is to:

- Verify correctness through unit tests
- Insert and search large datasets (~58k words)
- Validate rejection of prefix-only queries
- Benchmark performance on HPC using SLURM
- Plot insert/search time growth as dataset size increases

---

## 🛠️ Project Workflow

1. **TST Implementation**
   - Created `Node` and `TernarySearchTree` classes
   - Implemented `insert()`, `search()`, and `get_all_words()`

2. **Local Testing**
   - Sample word insertions: `"cat", "cape", "can", "dog", "dot"`
   - Checked:
     - Exact matches work ✅
     - Prefixes return false ❌
     - Empty strings ignored
     - Duplicates handled

3. **Dataset Integration**
   - Used `corncob_lowercase.txt` (58,110 English words)
   - Verified all words inserted and retrieved

4. **Negative Case Testing**
   - Used `not_insert_words.txt` to confirm no false matches

5. **GitHub Version Control**
   - Used branches, resolved merge conflicts
   - Pushed `.ipynb`, `.py`, benchmark, and SLURM script

6. **HPC Execution via SLURM**
   - Created virtualenv and activated it in the script
   - Converted `.ipynb` → `.py`
   - Submitted job using:
     ```bash
     sbatch -M genius tst_terenary.slurm
     ```

7. **Benchmarking**
   - Measured insert/search time for increasing word counts (step = 1000)
   - Plotted the results using `matplotlib`

8. **Time Complexity Analysis**
   - Analyzed actual vs theoretical complexity
   - Insert and Search scale nearly linearly

---

## 🧪 SLURM Output Snapshot


---

## 📊 Time Complexity of TST Operations

### 🔹 `insert(word)`
- Time complexity: **O(L × log N)**
- Each character goes one level deeper (L = word length)
- Binary tree logic on each node → log N comparisons

### 🔹 `search(word)`
- Time complexity: **O(L × log N)**
- Same traversal path as `insert()`, but no mutation

### 🔹 Space complexity
- **O(N × L)** in the worst case
  - N = number of unique words
  - L = average word length
- More compact than a trie; stores 1 char per node with 3 child links (left, middle, right)

---

## 📈 Performance Graph

- Benchmarked insert and search over 1,000 to 58,000 words
- Timed operations using `time.time()`
- Results show near-linear scaling in both operations
- Graph:
  - X-axis: number of words
  - Y-axis: time (seconds)
  - Blue: Insert
  - Green: Search

---

## 📁 Repository Structure
.
├── ternary_search_tree.py # Core TST implementation
├── benchmark_tst.py # Benchmarking insert/search
├── tst_terenary.slurm # SLURM HPC script
├── ternary-search-tree-project.ipynb # Notebook for dev/test
├── ternary_test.out # Output log from HPC job
├── requirements.txt # Dependencies
└── search_trees/
├── corncob_lowercase.txt # 58,110 English words
└── not_insert_words.txt # Negative test dataset

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

📦 Requirements

matplotlib
pip install -r requirements.txt


✅ Conclusion
This project successfully demonstrates the implementation, testing, and benchmarking of a Ternary Search Tree (TST) on both small and large datasets, using Python and VSC's Genius HPC cluster.

Key takeaways include:

Correct handling of insertions, searches, and negative cases

Scalability demonstrated through performance graphs

Practical SLURM job submission and resource usage on HPC

Solid grasp of data structure design and complexity analysis

This experience enhanced our understanding of algorithmic thinking, benchmarking, and real-world use of HPC in data science.