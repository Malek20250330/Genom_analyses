#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 1
#SBATCH --mem=4G
#SBATCH -t 01:00:00
#SBATCH -J makeblastdb_R7
#SBATCH --error=makeblastdb_R7.err
#SBATCH --output=makeblastdb_R7.out
#SBATCH --mail-user=mah_75420@yahoo.com
#SBATCH --mail-type=FAIL,END

# Load BLAST module
module load bioinfo-tools
module load blast/2.12.0+

# Input and output paths
FASTA="/home/mahtam/Genom_analyses/Processed_data/pilon_polished_R7/pilon_polished_R7.fasta"
OUTDIR="/home/mahtam/Genom_analyses/Processed_data/pilon_polished_R7"
DB_NAME="R7_db"

# Create the BLAST database
makeblastdb -in "$FASTA" \
            -dbtype nucl \
            -out "${OUTDIR}/${DB_NAME}" \
            -parse_seqids

echo "BLAST database created at ${OUTDIR}/${DB_NAME}.*"

