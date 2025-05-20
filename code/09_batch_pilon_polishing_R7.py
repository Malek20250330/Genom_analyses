#!/bin/bash -l

#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 2
#SBATCH --mem=16G
#SBATCH -t 03:30:00
#SBATCH -J pilon_polishing_R7
#SBATCH --mail-type=ALL
##SBATCH --mail-user your_email
#SBATCH --output=%x.%j.out

# Load modules

module load bioinfo-tools
module load bwa
module load samtools
module load Pilon/1.24


# Your commands

export ASSEMBLY_DIR=/home/mahtam/Genom_analyses/Processed_data/Flye_assembly_R7
export READS_DIR=/home/mahtam/Genom_analyses/trimmed_data/DNA_short_trim 
export OUTPUT_DIR=/home/mahtam/Genom_analyses/Processed_data/pilon_polished_R7
mkdir -p $OUTPUT_DIR

# Copy files to temporary directrory for processing
cp $ASSEMBLY_DIR/assembly_R7.fasta $SNIC_TMP/
cp $READS_DIR/SRR24413071* $SNIC_TMP/
cd $SNIC_TMP

# Index the genome
bwa index assembly_R7.fasta

# Map paired-end reads
bwa mem -v 3 -t 2 assembly_R7.fasta SRR24413071_1_trimmed.fastq.gz SRR24413071_2_trimmed.fastq.gz > aligned_R7_paired.sam

# Map unpaired reads seperately
bwa mem -v 3 -t 2 assembly_R7.fasta SRR24413071_1_unpaired.trimmed.fastq.gz > aligned_R7_unp1.sam
bwa mem -v 3 -t 2 assembly_R7.fasta SRR24413071_2_unpaired.trimmed.fastq.gz > aligned_R7_unp2.sam

# Convert SAM to BAM
samtools view -b aligned_R7_paired.sam > paired_R7.bam
samtools view -b aligned_R7_unp1.sam > unp1_R7.bam
samtools view -b aligned_R7_unp2.sam > unp2_R7.bam

# Merge unpaired BAM
samtools merge -@ 2 unpaired_R7.bam unp1_R7.bam unp2_R7.bam

# Sort and index
samtools sort -@ 2 -o paired_R7.sorted.bam paired_R7.bam
samtools index paired_R7.sorted.bam

samtools sort -@ 2 -o unpaired_R7.sorted.bam unpaired_R7.bam
samtools index unpaired_R7.sorted.bam

# Run pilon
java -Xmx16G -jar $PILON_HOME/pilon.jar \
  --genome assembly_R7.fasta \
  --frags paired_R7.sorted.bam \
  --unpaired unpaired_R7.sorted.bam \
  --output pilon_polished_R7 \
  --threads 2 \
  --changes \
  --vcf

# Copy results
cp pilon_polished_R7* $OUTPUT_DIR/
cp paired_R7.sorted.bam paired_R7.sorted.bam.bai unpaired_R7.sorted.bam unpaired_R7.sorted.bam.bai \
/proj/uppmax2025-3-3/nobackup/work/
 




