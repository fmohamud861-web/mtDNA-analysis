# Mitochondrial DNA Sequence Analysis

**Student:** Fardowsa Mohamud  
**Course:** Bioinformatics / Biological Databases  
**Date:** March 10, 2026  

---

# Project Overview

This project analyzes mitochondrial DNA (mtDNA) sequences retrieved from the NCBI biological database. The goal of this analysis was to demonstrate how bioinformatics tools can be used to retrieve, process, analyze, and visualize biological sequence data using Python.

Mitochondrial DNA is essential for cellular energy production and is widely studied in genetics, evolutionary biology, and medical research. By analyzing sequence characteristics such as GC content and sequence length, we can gain insights into the composition and variability of mitochondrial sequences.

This project combines biological databases, Python programming, and data visualization to perform automated sequence analysis.

---

# Project Objectives

The main objectives of this project were:

1. Retrieve mitochondrial DNA sequences from the NCBI database.
2. Process sequence data using Python and Biopython.
3. Perform computational analyses on the sequences.
4. Visualize the results using graphical plots.
5. Create an interactive visualization as part of the bonus challenge.
6. Document the workflow in a professional GitHub repository.

---

# Project Workflow

The workflow for this project consisted of the following steps:

### 1. Data Retrieval
DNA sequences were retrieved from the NCBI database using Python scripts that access biological sequence records.

### 2. Data Processing
Sequences were processed using the Biopython library. Each sequence was parsed and analyzed to extract key metrics.

### 3. Sequence Analysis
Two analyses were performed:

• **GC Content Analysis**  
The percentage of guanine (G) and cytosine (C) nucleotides in each sequence was calculated.

• **Sequence Length Analysis**  
The total nucleotide length of each sequence was calculated.

### 4. Data Visualization
Python libraries such as Matplotlib were used to generate visualizations of the results.

### 5. Interactive Visualization (Bonus)
An interactive visualization was created using Plotly to allow dynamic exploration of the dataset.

---

# Project Files

This repository contains the following files:

| File | Description |
|-----|-------------|
| final_analysis.py | Main Python script used for sequence retrieval and analysis |
| interactive_plot.py | Python script used to generate the interactive Plotly visualization |
| data.csv | Processed dataset used for plotting |
| figure1.png | Histogram showing GC content distribution |
| figure2.png | Histogram showing sequence length distribution |
| interactive_plot.html | Interactive visualization that can be opened in a web browser |
| analysis_report.md | Detailed project report explaining the analysis |
| README.md | Documentation and project overview |

---

# Visualizations

## GC Content Distribution

![GC Content Histogram](figure1.png)

This figure shows the distribution of GC content across the mitochondrial DNA sequences analyzed in this project.

---

## Sequence Length Distribution

![Sequence Length Histogram](figure2.png)

This figure shows how sequence lengths vary across the dataset.

---

# Interactive Visualization (Bonus)

This project also includes an **interactive Plotly visualization**.

The interactive plot allows users to:

• Hover over data points  
• Zoom in and out of the plot  
• Explore sequence statistics dynamically  

To view the interactive visualization:

Download and open:interactive_plot.html


in any web browser.
## How to Access the GitHub Repository

This project has been uploaded to GitHub as part of the optional bonus challenge.

To access the repository:

1. Open a web browser.
2. Go to the following link:

https://github.com/fmohamud861-web/mtDNA-analysis

3. The repository contains all project files including:
   - Python analysis scripts
   - Data used for the analysis
   - Figures generated from the analysis
   - The interactive visualization
   - Project documentation

---

# How to Run the Analysis

## Step 1 – Navigate to the project directory
cd ~/week7

## Step 2 – Install required Python packages
pip3 install biopython pandas matplotlib plotly

## Step 3 – Run the main analysis script
python3 final_analysis.py

This script will:

• Retrieve mitochondrial DNA sequences  
• Perform GC content analysis  
• Calculate sequence lengths  
• Generate plots and save results  

---

# Example Output

Running the script produces:

• `data.csv` – processed dataset  
• `figure1.png` – GC content histogram  
• `figure2.png` – sequence length histogram  

The bonus script generates:

• `interactive_plot.html`

---

# Reflection

This project helped demonstrate how biological databases and computational tools can be integrated to analyze genetic data. By using Python and bioinformatics libraries, it was possible to automate data retrieval, perform sequence analysis, and generate visualizations efficiently.

This type of workflow is commonly used in bioinformatics research when working with large biological datasets. Learning how to retrieve data programmatically and analyze it using scripts is an important skill for modern biological research and data-driven healthcare applications.

---

# AI Use Disclosure

AI Tool Used: ChatGPT

Purpose of AI Use:
AI assistance was used to help structure the Python scripts, troubleshoot errors, and assist in formatting documentation for the project.

Verification Process:
All code and outputs were tested on the AWS server to ensure that the scripts executed correctly, generated the expected output files, and satisfied the assignment requirements.
