# OligoGen: Custom In-Silico Oligonucleotide Library Generator

OligoGen is a Python-based tool designed for generating **randomized oligonucleotide sequences** with **user-defined nucleotide compositions**. This script enables researchers to simulate **combinatorial oligonucleotide libraries**, such as **aptamer pools for SELEX experiments**, by specifying custom base ratios at different positions within a sequence. It outputs sequences in **FASTA format**, making it easy to integrate into **bioinformatics pipelines** and **computational modeling workflows**.

## **Features**
✅ Generate **random oligonucleotide sequences** with precise base ratios (e.g., A:C:G:T = 50:0:50:0).  
✅ Support for **custom nucleotide patterns** (e.g., `N(50005000)`) to create **complex combinatorial libraries**.  
✅ Output sequences in **FASTA format**, compatible with standard **NGS workflows and computational tools**.  
✅ Ideal for **simulating aptamer libraries, exploring sequence diversity, and in-silico SELEX applications**.  

---

## **Installation**
This script requires **Python 3**. Clone the repository and run it locally:

git clone https://github.com/YourUsername/OligoGen.git
cd OligoGen
python oligo_generator.py

### The script will prompt for:
1.	Oligonucleotide sequence pattern
	- Example: N(50005000)ATCGN
2.	Number of sequences to generate
	- Example: 100
3.	Output file name
	- Example: sequences.fasta

## **Example Run**
```
$ python oligo_generator.py
Enter your oligonucleotide sequence: N(50005000)ATCGN
Enter the number of sequences to generate: 100
Enter the output file name: sequences.fasta
Generating 100 sequences...
100 sequences saved to sequences.fasta in FASTA format.
```

### Example FASTA Output
```
>Seq_1
GATCGG
>Seq_2
AATCGT
>Seq_3
GATCGG
>Seq_4
TATCGA
>Seq_5
GGTCCA
...
```
The generated sequences will be saved in a FASTA file for easy integration into bioinformatics workflows.
