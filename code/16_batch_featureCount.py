#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 8
#SBATCH --mem=16G
#SBATCH -t 20:00:00
#SBATCH -J featureCounts
#SBATCH --mail-user
#SBATCH --output=%x.%j.out

set -e  # Exit on error
set -x  # Print commands

# Load modules
module load bioinfo-tools
module load subread  # contains featureCounts
#module load samtools  # for header inspection

# Set paths
export INPUT_HP_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_HP126
export INPUT_R_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_R7
export GFF_DIR=/home/mahtam/Genom_analyses/Annotation_data/Prokka_annotation_R7
export OUTPUT_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/FeatureCounts
#mkdir -p $OUTPUT_DIR


# Copy data to temporary directory
#cp $INPUT_HP_DIR/*.sorted.bam $SNIC_TMP/
cp $INPUT_R_DIR/*.sorted.bam $SNIC_TMP/
cp $GFF_DIR/R7_annotation.gff $SNIC_TMP/
cd $SNIC_TMP


##featureCounts -h

# For HP and R7
for SAMPLE in *.sorted.bam
do
 BASENAME=$(basename "$SAMPLE" .sorted.bam)

featureCounts -T 8 -p -t gene -g ID \
  -a R7_annotation.gff \
  -o ${BASENAME}_counts.txt \
  $SAMPLE \
  2> ${BASENAME}_featureCounts.log

  cp ${BASENAME}_counts.txt $OUTPUT_DIR/
  cp ${BASENAME}_counts.txt.summary $OUTPUT_DIR/
  cp ${BASENAME}_featureCounts.log $OUTPUT_DIR/

done

# Final success message

echo "All featureCounts jobs completed successfully at $(date)"

