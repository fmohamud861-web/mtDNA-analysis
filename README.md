# Assignment 7 – Human Mitochondrial DNA Analysis

## Purpose of This Project

The purpose of this project is to retrieve and analyze human mitochondrial DNA (mtDNA) sequences using Python and RESTful APIs. Mitochondrial DNA is maternally inherited and plays a key role in energy production and genetic studies.  

This project performs the following main tasks:

1. Retrieves 100 human mitochondrial DNA sequences from the NCBI Nucleotide database using the Entrez API  
2. Calculates GC content and sequence length for each sequence  
3. Generates two histograms to visualize GC content and sequence length  
4. (Bonus) Creates an interactive scatter plot of GC content versus sequence length using Plotly  

---

## Files Included

- `final_analysis.py`  
  Main Python script. Running this file performs sequence retrieval, calculations, and generates visualizations.

- `interactive_plot.py` (optional bonus)  
  Reads the processed CSV and creates an interactive scatter plot.

- `data.csv`  
  Contains processed sequence data with columns: `sequence_length` and `gc_content`.

- `figure1.png`  
  Histogram of GC content distribution.

- `figure2.png`  
  Histogram of sequence length distribution.

- `interactive_plot.html` (optional bonus)  
  Interactive scatter plot of GC content vs sequence length.

- `README.md`  
  Documentation, project workflow, and reflection (this file).

---

## How to Run the Scripts

### Step 1: Navigate to the project folder
```bash
cd ~/week7
### Step 2: Confirm files exist
ls -la
You should see final_analysis.py,interactive_plot.py, and other output files.
### Step 3: Install required packages (only once)
pip3 install biopython pandas matplotlib plotly requests
### Step 4: Run the main analysis
python3 final_analysis.py
### Step 5: Run the interactive visualization (optional bonus)
python3 interactive_plot.py

### Expected Output
When running the scripts, you should see messages such as:

- STEP 1: Retrieving sequences from NCBI…

STEP 2: Calculating GC content and sequence lengths…

STEP 3: Generating histograms…

Script completed successfully!

The scripts will produce:

data.csv with GC content and sequence lengths

figure1.png (GC content distribution)

figure2.png (sequence length distribution)

interactive_plot.html (interactive scatter plot, optional)


## Reflection
What I Learned About Bioinformatics APIs

This project taught me how to programmatically retrieve real biological data using the NCBI Entrez API. I learned how sequences are structured in FASTA format and how to extract meaningful information such as GC content and sequence length. Automating these steps with Python allows for efficient, reproducible analysis of large datasets.

The Most Challenging Part and How I Solved It

The most challenging part was handling sequence data formatting and calculating GC content consistently, especially with partial sequences. I solved this by writing reusable Python functions and verifying results by comparing sequences manually. Creating visualizations that accurately reflect the data also required testing and adjusting bins in histograms.

Connection to My Future Work

This project strengthened my understanding of computational biology workflows. Instead of manually analyzing sequences, I can now use APIs and Python scripts to explore genomic features at scale. This is a key skill for bioinformatics, genomics research, and healthcare data analysis.

## AI Use Disclosure:

AI tool used: ChatGPT

What I used it for: Assisting in structuring Python scripts, writing this README/report, and suggesting workflow and visualization approaches.

How I verified/edited the output: All scripts were run on the AWS server to verify correct sequence retrieval, data processing, and figure generation. I reviewed the code and outputs to ensure they met assignment requirements.
