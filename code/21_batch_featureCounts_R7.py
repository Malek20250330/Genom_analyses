#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 8
#SBATCH --mem=16G
#SBATCH -t 04:00:00
#SBATCH -J featureCounts_split_R7
#SBATCH --output=%x.%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mah_75420@yahoo.com   # OPTIONAL: set your email

module load bioinfo-tools
module load subread/2.0.3  # or just subread if version doesn't matter

# Paths
export BAM_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_R7_realign
export GFF=/home/mahtam/Genom_analyses/Annotation_data/Prokka_annotation_R7/R7_annotation.gff
export OUTPUT_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/FeatureCounts

mkdir -p "$OUTPUT_DIR"

# Run featureCounts individually on each BAM file
cd "$BAM_DIR"

for BAM in SRR24516462_R7_realigned.sorted.bam SRR24516463_R7_realigned.sorted.bam SRR24516464_R7_realigned.sorted.bam; do
    SAMPLE_NAME=$(basename "$BAM" .sorted.bam)
    echo "Running featureCounts for $SAMPLE_NAME"
    
    featureCounts -T 4 -p -t gene -g ID \
      -a "$GFF" \
      -o "$OUTPUT_DIR/${SAMPLE_NAME}_counts.txt" \
      "$BAM"
done

echo "All featureCounts runs completed at $(date)"


