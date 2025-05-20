#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 8
#SBATCH --mem=16G
#SBATCH -t 04:00:00
#SBATCH -J blastn_HP126_vs_R7
#SBATCH --error=blastn_HP126_vs_R7.err
#SBATCH --mail-user=mah_75420@yahoo.com
#SBATCH --output=blastn_HP126_vs_R7.out
#SBATCH --mail-type=ALL  # Optional: get notified when job starts, ends, fails, etc.

# Load BLAST module
module load bioinfo-tools
module load blast/2.12.0+  # Adjust version if needed

# Set working directories
QUERY="/home/mahtam/Genom_analyses/Processed_data/pilon_polished_HP126/pilon_polished_HP126.fasta"
DB_DIR="/home/mahtam/Genom_analyses/Processed_data/pilon_polished_R7"
OUTDIR="/home/mahtam/Genom_analyses/Result/Compare"
OUTFILE="${OUTDIR}/HP126_vs_R7_blast.txt"

# Create output directory if it doesn't exist
mkdir -p "$OUTDIR"

# Run BLAST
blastn -query "$QUERY" \
       -db "${DB_DIR}/R7_db" \
       -out "$OUTFILE" \
       -evalue 1e-10 \
       -num_threads 8 \
       -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"

echo "BLASTN finished"






