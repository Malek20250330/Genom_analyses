#!/bin/bash -l

#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 4
#SBATCH --mem=16G
#SBATCH -t 06:30:00
#SBATCH -J Flye_assembly_DNA_HP126
#SBATCH --mail-type=ALL
##SBATCH --mail-user your_email
#SBATCH --output=%x.%j.out

# Load modules

module load bioinfo-tools Flye/2.9.5


# Your commands

export INPUT_DIR=/home/mahtam/2_Beganovic_2023/DNA_reads 
export OUTPUT_DIR=/home/mahtam/Genom_analyses/Processed_data/Flye_assembly_HP126
mkdir -p $OUTPUT_DIR

# Copy files to temporary directrory for processing
cp $INPUT_DIR/SRR24413066.fastq.gz $SNIC_TMP/ 
cd $SNIC_TMP

# Process each sample

flye -t 4 --nano-raw SRR24413066.fastq.gz --min-overlap 2000 --out-dir $OUTPUT_DIR



# Copy the output files back to the trimmed director
cp -r $SNIC_TMP/* $OUTPUT_DIR/



