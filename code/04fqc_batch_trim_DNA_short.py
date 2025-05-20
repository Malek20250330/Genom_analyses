#!/bin/bash -l
#SBATCH -A uppmax2025-3-3    # Project name
#SBATCH -M snowy             # Cluster name
#SBATCH -p core              # Partition (queue)
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH -t 01:00:00          # Time limit (HH:MM:SS)
#SBATCH -J fqc_trimmed_DNA_short	  # Job name
#SBATCH --mail-user=mah_75420@yahoo.com	   #email notification
#SBATCH --output=%x.%j.out
##SBATCH --reservation=uppmax2025-3-3_1


# Load modules
module load bioinfo-tools FastQC/0.11.9

# Define input directory
export INPUT_DIR=/home/mahtam/Genom_analyses/trimmed_data/DNA_short_trim
export OUTPUT_DIR=/home/mahtam/Genom_analyses/fastqc_trim
mkdir -p $OUTPUT_DIR

# Copy files to temporary directory for processing
cp $INPUT_DIR/*fastq.gz $SNIC_TMP/
cd $SNIC_TMP

# Run FastQC on each of the specified files

for i in 65 71
do
    fastqc -t 2 -o $OUTPUT_DIR SRR244130"$i"_*.fastq.gz
done


# Copy the output files back to the results director
#cp *.zip *.html $OUTPUT_DIR/

