#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 8
#SBATCH --mem=16G
#SBATCH -t 04:00:00
#SBATCH -J featureCounts_fixed
#SBATCH --output=%x.%j.out

module load bioinfo-tools
module load subread

# Paths
export BAM_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_R7_realign
export GFF=/home/mahtam/Genom_analyses/Annotation_data/Prokka_annotation_R7/R7_annotation.gff
export OUTPUT_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/FeatureCounts
mkdir -p $OUTPUT_DIR

# Run featureCounts
cd $BAM_DIR
featureCounts -T 8 -p -t gene -g ID \
  -a $GFF \
  -o $OUTPUT_DIR/featureCounts_R7.txt \
  *.bam

echo "featureCounts completed at $(date)"

