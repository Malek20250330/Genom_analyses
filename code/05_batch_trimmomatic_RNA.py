#!/bin/bash -l

#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 2
#SBATCH -t 01:30:00
#SBATCH -J T1_RNA_reads
#SBATCH --mail-type=ALL
##SBATCH --mail-user your_email
#SBATCH --output=%x.%j.out

# Load modules

module load bioinfo-tools trimmomatic


# Your commands

export INPUT_DIR=/home/mahtam/2_Beganovic_2023/RNA_reads/ 
export OUTPUT_DIR=/home/mahtam/Genom_analyses/trimmed_data/RNA_trim
mkdir -p $OUTPUT_DIR

# Copy files to temporary directrory for processing
cp $INPUT_DIR/*fastq.gz $SNIC_TMP/ 
cd $SNIC_TMP

# Process each sample
for i in {56..64}
do
	trimmomatic PE -phred33 \
SRR245164"$i"_1.fastq.gz SRR245164"$i"_2.fastq.gz \
SRR245164"$i"_1_trimmed_RNA.fastq.gz SRR245164"$i"_2_trimmed.fastq.gz \
SRR245164"${i}"_1_unpaired_trimmed_RNA.fastq.gz SRR245164"${i}"_2_unpaired_trimmed_RNA.fastq.gz \
ILLUMINACLIP:$TRIMMOMATIC_HOME/adapters/TruSeq3-PE.fa:2:30:10 \
LEADING:20 TRAILING:20 MINLEN:36 \
-threads 2
done

# Copy the output files back to the trimmed director
cp *trimmed_RNA.fastq.gz  $OUTPUT_DIR/



