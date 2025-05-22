#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 4
#SBATCH --mem=32G
#SBATCH -t 02:00:00
#SBATCH -J quast_R7
#SBATCH --mail-user=mah_75420@yahoo.com
#SBATCH --output=%x.%j.out

# Load modules
module load bioinfo-tools
module load quast/5.0.2

# Set paths
export INPUT_DIR=/home/mahtam/Genom_analyses/Processed_data/pilon_polished_R7
export REF_DIR=/home/mahtam/2_Beganovic_2023/reference_genome
export OUTPUT_DIR=/home/mahtam/Genom_analyses/Processed_data/Assembly_validation_R7_Quest
mkdir -p $OUTPUT_DIR

# Copy files to temporary directory
cp $INPUT_DIR/pilon_polished_R7.fasta $SNIC_TMP/
cp $REF_DIR/R7_genome.fasta $SNIC_TMP/
cd $SNIC_TMP

# Run QUAST
quast.py pilon_polished_R7.fasta \
  -r R7_genome.fasta \
  -o quast_results_R7 \
  -t 4 \
  --min-contig 200

# Copy results back
cp -r quast_results_R7 $OUTPUT_DIR/

