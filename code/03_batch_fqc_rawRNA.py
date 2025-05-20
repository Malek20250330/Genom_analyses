#!/bin/bash -l

#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 2
#SBATCH -t 01:30:00
#SBATCH -J Q2
#SBATCH --mail-type=ALL
##SBATCH --mail-user your_email
#SBATCH --output=%x.%j.out

# Load modules

module load bioinfo-tools
module load FastQC

# Your commands

fastqc ../2_Beganovic_2023/DNA_reads/RNA_reads/*.gz -o /home/mahtam/Genom_analyses/fastqc_raw/RNA_short_qc 


