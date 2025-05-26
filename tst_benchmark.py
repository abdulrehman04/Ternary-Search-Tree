import time
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree

# Load word list (adjust path if needed)
with open("data/search_trees/corncob_lowercase.txt") as f:
    words = [line.strip() for line in f if line.strip()]

sample_sizes = [100, 500, 1000, 5000, 10000, 20000]
insert_times = []
search_times = []

for size in sample_sizes:
    tst = TernarySearchTree()
    test_words = words[:size]

    # Time insert
    start = time.time()
    for word in test_words:
        tst.insert(word)
    insert_duration = time.time() - start
    insert_times.append(insert_duration)

    # Time search (search all inserted words)
    start = time.time()
    for word in test_words:
        tst.search(word, exact=True)
    search_duration = time.time() - start
    search_times.append(search_duration)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, insert_times, label="Insert Time (s)", marker="o")
plt.plot(sample_sizes, search_times, label="Search Time (s)", marker="x")
plt.xlabel("Number of Words")
plt.ylabel("Time (seconds)")
plt.title("Ternary Search Tree Benchmark")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("benchmark_plot.png")
print("Benchmark completed and plot saved.")
