# 🌲 Ternary Search Tree (TST) — Implementation & Benchmarking

This project implements a *Ternary Search Tree (TST)* from scratch in Python and benchmarks its performance across varying word list sizes. Benchmarking was executed on *Local* as well as on the *KU Leuven Tier-2 HPC - wICE cluster*.

---

## 🧠 Project Goals

- Build a character-efficient Ternary Search Tree
- Benchmark insert and search operations at scale
- Use VSC's HPC to evaluate performance under large inputs

---

## 🗂️ Directory Structure

bash
.
├── data/                          # Input dictionary (word list)
├── benchmark_plot.png            # Output benchmark plot
├── main_job.slurm                # SLURM job script for HPC
├── ternary_search_tree.ipynb     # Usage + test notebook