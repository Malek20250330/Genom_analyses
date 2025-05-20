#!/bin/bash -l

#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 2
#SBATCH -t 01:30:00
#SBATCH -J T1_DNA_short
#SBATCH --mail-type=ALL
##SBATCH --mail-user your_email
#SBATCH --output=%x.%j.out

# Load modules

module load bioinfo-tools trimmomatic


# Your commands

export INPUT_DIR=/home/mahtam/2_Beganovic_2023/DNA_reads/short_reads/ 
export OUTPUT_DIR=/home/mahtam/Genom_analyses/trimmed_data/DNA_short_trim
mkdir -p $OUTPUT_DIR

# Copy files to temporary directrory for processing
cp $INPUT_DIR/*fastq.gz $SNIC_TMP/ 
cd $SNIC_TMP

# Process each sample
for i in 65 71
do
	trimmomatic PE -phred33 \
SRR244130"$i"_1.fastq.gz SRR244130"$i"_2.fastq.gz \
SRR244130"$i"_1_trimmed.fastq.gz SRR244130"$i"_2_trimmed.fastq.gz \
SRR244130"$i"_1_unpaired.trimmed.fastq.gz SRR244130"$i"_2_unpaired.trimmed.fastq.gz \
ILLUMINACLIP:$TRIMMOMATIC_HOME/adapters/TruSeq3-PE.fa:2:30:10 \
LEADING:20 TRAILING:15 MINLEN:100 \
-threads 2
done

# Copy the output files back to the trimmed director
cp *trimmed.fastq.gz *unpaired.trimmed.fastq.gz $OUTPUT_DIR/



