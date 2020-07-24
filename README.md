# FASTQ-to-FASTA
# A program by Tyler Serio
# What is it?
FASTQ to FASTA

# What does it do?
This program converts FASTQ files to FASTA files.

# How does it do it?
This program walks through a FASTQ file, copying the first two lines and placing them into a new FASTA output file.

# Why was it written?
This program was written to quickly convert FASTQ files to FASTA files, a common need for many bioinformatics pipelines. This process can take a long time if you are uploading large FASTQ files to a website to convert the sequences for you, and so to make things more efficient this conversion can be performed rapidly with this simple available program instead.

# Notes
The symbol ">" is sometimes needed in front of the query ID line in a FASTA file. The way that this program runs now, the ">" is not added. If your FASTQ file already contains the ">" character it will be recorded in the FASTA file, however, it will not be added if it is not already present in the FASTQ input file.
