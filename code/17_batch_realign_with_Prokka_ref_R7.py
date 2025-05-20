#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 4
#SBATCH --mem=16G
#SBATCH -t 20:00:00
#SBATCH -J realign_with_prokka_ref
#SBATCH --output=%x.%j.out

set -e
set -x

# Load modules
module load bioinfo-tools
module load bwa/0.7.18
module load samtools/1.16

# Paths
export READ_DIR=/home/mahtam/2_Beganovic_2023/RNA_reads
export PROKKA_DIR=/home/mahtam/Genom_analyses/Annotation_data/Prokka_annotation_R7
export OUTPUT_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_R7_realign
mkdir -p $OUTPUT_DIR

# Copy Prokka reference genome and reads to SNIC_TMP
cp $PROKKA_DIR/R7_annotation.fna $SNIC_TMP/
cp $READ_DIR/SRR24516462*.fastq.gz $SNIC_TMP/
cp $READ_DIR/SRR24516463*.fastq.gz $SNIC_TMP/
cp $READ_DIR/SRR24516464*.fastq.gz $SNIC_TMP/
cd $SNIC_TMP

# Index reference
bwa index R7_annotation.fna

# Align reads using Prokka-compatible reference
for SAMPLE in SRR24516462 SRR24516463 SRR24516464
do
  bwa mem R7_annotation.fna ${SAMPLE}_1.fastq.gz ${SAMPLE}_2.fastq.gz > ${SAMPLE}.sam
  samtools view -Sb ${SAMPLE}.sam > ${SAMPLE}.bam
  samtools sort ${SAMPLE}.bam -o ${SAMPLE}_R7.fixed.sorted.bam
  samtools index ${SAMPLE}_R7.fixed.sorted.bam

  # Copy results back
  cp ${SAMPLE}_R7.fixed.sorted.bam $OUTPUT_DIR/
  cp ${SAMPLE}_R7.fixed.sorted.bam.bai $OUTPUT_DIR/
done

echo "Realignment finished at $(date)"

