#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 8
#SBATCH --mem=16G
#SBATCH -t 20:00:00
#SBATCH -J featureCounts_HP126
#SBATCH --mail-user=mah_75420@yahoo.com
#SBATCH --output=%x.%j.out

set -e
set -x

# Load modules
module load bioinfo-tools
module load subread

# Set paths
export BAM_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_HP126_realigned
export GFF_FILE=/home/mahtam/Genom_analyses/Annotation_data/Prokka_annotation_HP126/HP126_annotation.gff
export OUTPUT_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/FeatureCounts
mkdir -p $OUTPUT_DIR

# Copy files to tmp
cp $BAM_DIR/*.sorted.bam $SNIC_TMP/
cp $GFF_FILE $SNIC_TMP/
cd $SNIC_TMP

# Run featureCounts on each BAM
for BAM in *.sorted.bam; do
  SAMPLE=$(basename "$BAM" .sorted.bam)

  featureCounts -T 8 -p -t gene -g ID \
    -a $(basename "$GFF_FILE") \
    -o ${SAMPLE}_counts.txt \
    $BAM \
    2> ${SAMPLE}_featureCounts.log

  # Copy results back
  cp ${SAMPLE}_counts.txt $OUTPUT_DIR/
  cp ${SAMPLE}_counts.txt.summary $OUTPUT_DIR/
  cp ${SAMPLE}_featureCounts.log $OUTPUT_DIR/
done

echo "FeatureCounts finished successfully for HP126."




















