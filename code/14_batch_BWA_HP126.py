#!/bin/bash -l
#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 1
#SBATCH --mem=16G
#SBATCH -t 20:00:00
#SBATCH -J BWA_HP126
#SBATCH --mail-user
#SBATCH --output=%x.%j.out

set -e
set -x

# Load modules
module load bioinfo-tools
module load bwa/0.7.18
module load samtools

# Set paths
export INPUT_DIR=/home/mahtam/2_Beganovic_2023/RNA_reads
export REF_DIR=/home/mahtam/Genom_analyses/Processed_data/pilon_polished_R7
export OUTPUT_DIR=/proj/uppmax2025-3-3/GAP2_mahtab/BWA_HP126
mkdir -p $OUTPUT_DIR

# Copy data to temporary directory
cp $INPUT_DIR/SRR24516459*.fastq.gz $INPUT_DIR/SRR24516460*.fastq.gz \
   $INPUT_DIR/SRR24516461*.fastq.gz $SNIC_TMP/
cp $REF_DIR/pilon_polished_R7.fasta $SNIC_TMP/
cd $SNIC_TMP

# Fix contig names in the reference FASTA to match GFF
sed 's/^>contig_3_pilon/>gnl|Prokka|DCFNGNFD_1/' pilon_polished_R7.fasta | \
sed 's/^>contig_1_pilon/>gnl|Prokka|DCFNGNFD_2/' > fixed_reference.fasta

# Index corrected reference genome
bwa index fixed_reference.fasta

# Align reads and process BAM
for SAMPLE in SRR24516459 SRR24516460 SRR24516461
do
  if [ -f ${SAMPLE}_1.fastq.gz ] && [ -f ${SAMPLE}_2.fastq.gz ]; then
    bwa mem fixed_reference.fasta ${SAMPLE}_1.fastq.gz ${SAMPLE}_2.fastq.gz > ${SAMPLE}.sam
    samtools view -Sb ${SAMPLE}.sam > ${SAMPLE}.bam
    samtools sort ${SAMPLE}.bam -o ${SAMPLE}_HP126.sorted.bam
    samtools index ${SAMPLE}_HP126.sorted.bam

    # Save outputs
    cp ${SAMPLE}.sam $OUTPUT_DIR/
    cp ${SAMPLE}_HP126.sorted.bam $OUTPUT_DIR/
    cp ${SAMPLE}_HP126.sorted.bam.bai $OUTPUT_DIR/
  else
    echo "Missing reads for ${SAMPLE}"
  fi
done

