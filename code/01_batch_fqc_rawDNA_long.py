#!/bin/bash -l

#SBATCH -A uppmax2025-3-3
#SBATCH -M snowy
#SBATCH -p core
#SBATCH -n 2
#SBATCH -t 02:30:00
#SBATCH -J Q1
#SBATCH --mail-type=ALL
##SBATCH --mail-user your_email
#SBATCH --output=%x.%j.out

# Load modules

module load bioinfo-tools
module load FastQC

# Your commands

#fastqc -t 2 ../../2_Beganovic_2023/DNA_reads/*.fastq.gz -o /home/mahtam/Genom_analyses/fastqc_raw/DNA_long_qc 
export Input_Dir=/home/mahtam/2_Beganovic_2023/DNA_reads

export Output_Dir=/home/mahtam/Genom_analyses/fastqc_raw/DNA_long_qc

cp $Input_Dir/*fastq.gz $SNIC_TMP/
cd $SNIC_TMP

# set java option to increase heap space
export FASTQC_JAVA_OPTIONS="-Xmx16G"

# Run FastQC on each of the specified files

for i in {66,72};
do

	fastqc -t 2 -o $Output_Dir SRR244130"$i".fastq.gz
done

cp *fastq* $Output_Dir

