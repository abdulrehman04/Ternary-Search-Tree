#!/bin/bash
#SBATCH --job-name=benchmark_test
#SBATCH --output=output_%j.txt
#SBATCH --error=error_%j.txt
#SBATCH --time=00:30:00
#SBATCH --mem=4G
#SBATCH --ntasks=1

# Load libraries
module load cluster/wice/interactive
module load matplotlib/3.9.2-gfbf-2024a


# Run your benchmark script
python tst_benchmark.py
