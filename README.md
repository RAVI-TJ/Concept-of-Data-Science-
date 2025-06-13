# 🔍 Ternary Search Tree (TST) – HPC-Based Data Science Project (2024–2025)

## 🎓 Master's Project – Concepts of Data Science  
**Student 1:** NUTHI RAVITEJA PEDIREDLA 
**Student 2:**
**Course:** Concepts of Data Science  
**University:** HASSELT UNIVERSITY   
**Cluster Used:** Genius (VSC HPC)

---

## 📘 Overview

This project implements a **Ternary Search Tree (TST)** for efficient word storage and retrieval. The goal is to validate the data structure’s correctness, evaluate performance on a large dataset, and execute it at scale using **HPC (High Performance Computing)** infrastructure via **SLURM**.

The TST was benchmarked using a dataset of over **58,000 English words**, and the performance (insert and search time) was plotted to analyze complexity growth.

---

## 🛠️ Project Workflow

1. **Designed and Implemented TST in Python**
   - Defined `Node` and `TernarySearchTree` classes with:
     - `insert(word)`
     - `search(word)`
     - `get_all_words()`

2. **Tested Core Functionalities Locally**
   - Inserted sample words (`cat`, `cape`, `can`, etc.)
   - Checked correctness of:
     - Exact match (`search('cat')` → ✅)
     - Prefix rejection (`search('ca')` → ❌)
     - Empty string input
     - Duplicate inserts

3. **Loaded and Inserted Dataset**
   - Used `corncob_lowercase.txt` containing **58,110 English words**
   - Ensured all words inserted and retrieved using `get_all_words()`

4. **Negative Case Testing**
   - Used `not_insert_words.txt` to verify that invalid/unseen words are not mistakenly matched by the tree

5. **Pushed Code to GitHub**
   - Committed all code updates, test cases, `.ipynb` and `.py` scripts
   - Resolved merge conflicts using Git and Vim
   - Ensured collaborative history and instructor access

6. **Executed Code on HPC with SLURM**
   - Converted `.ipynb` to `.py` using `nbconvert`
   - Wrote and debugged `tst_terenary.slurm` SLURM job script
   - Solved issues:
     - Windows line endings (`\r\n`)
     - Invalid account errors (`--account` fix)
     - Missing cluster spec (`--clusters=genius`)
   - Successfully ran benchmark job using:
     ```bash
     sbatch -M genius tst_terenary.slurm
     ```

7. **Benchmarked Insert & Search**
   - Benchmarked performance for growing word counts (steps of 1000)
   - Recorded `insert()` and `search()` times
   - Generated a performance graph using `matplotlib`

8. **Plotted Time Complexity Graph**
   - `insert()` and `search()` both show near-linear scaling
   - Confirmed complexity matches theoretical analysis

---

## 📁 Repository Structure


---

## 🧪 Test Cases Overview

| Test Case                  | Result     |
|---------------------------|------------|
| Insert valid word         | ✅ Success |
| Search full word match    | ✅ Found   |
| Search prefix (invalid)   | ❌ Rejected|
| Insert empty string       | ✅ Ignored |
| Insert duplicates         | ✅ Handled |
| Words from not_insert_words.txt | ✅ Not Found |
| Total words inserted      | ✅ 58,110  |

---

## 📊 Performance Benchmark

### ✅ Graph: Insert vs Search Time

- Benchmarked for 1,000 → 58,000 words
- Used `time.time()` for each batch
- Results plotted with `matplotlib`

### 📈 Sample Graph Behavior

- **X-axis**: Number of inserted words
- **Y-axis**: Time (in seconds)
- 🔵 Insert time grows gradually
- 🟢 Search time also scales linearly

---

## ⏱️ Time & Space Complexity

| Operation | Time Complexity   | Space Complexity |
|-----------|------------------|------------------|
| Insert    | O(L × log N)     | O(N)             |
| Search    | O(L × log N)     | O(1)             |

Where:
- `L`: Length of the word
- `N`: Number of nodes in the TST

---

## 🖥️ HPC Execution (SLURM)

### SLURM Script Snippet:

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

This project successfully demonstrates the implementation, testing, and performance evaluation of a Ternary Search Tree (TST) data structure using Python and HPC infrastructure. By working with both small and large datasets (over 58,000 words), the TST proved to be efficient and scalable for word search applications.

The project workflow—from initial function development and local testing, through dataset validation and Git version control, to SLURM job submission on the Genius cluster—provided deep insights into real-world data structure analysis and high-performance computing.

The benchmark results and complexity analysis confirmed that both insertion and search operations scale near-linearly, validating the theoretical expectations of TSTs. Prefix-based rejection and negative-case testing ensured robustness and correctness.

Overall, this project combined data science theory, efficient algorithm design, and practical HPC skills, offering a well-rounded, research-driven learning experience as part of a Master's-level academic curriculum.