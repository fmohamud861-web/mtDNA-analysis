# Mitochondrial DNA Sequence Analysis Project

**Student:** Fardowsa Mohamud  
**Course:** Bioinformatics / Biological Databases  
**Project:** mtDNA Sequence Analysis  
**Date:** March 10, 2026

---

# Introduction

Mitochondrial DNA (mtDNA) plays an important role in cellular energy production and is widely studied in genetics, evolutionary biology, and medical research. Unlike nuclear DNA, mitochondrial DNA is inherited maternally and contains genes that are essential for oxidative phosphorylation.

The purpose of this project was to retrieve mitochondrial DNA sequence data from a biological database and perform computational analysis using Python. By analyzing sequence characteristics such as GC content and sequence length, we can better understand patterns within mitochondrial sequences and how they may vary across datasets.

This project demonstrates how programming and biological databases can be combined to automate data retrieval, analysis, and visualization.

---

# Methods

## Data Retrieval

The dataset used in this project was retrieved from the NCBI database using Python. The script accessed sequence data through NCBI's Entrez utilities and downloaded mitochondrial DNA sequences for analysis.

These sequences were then parsed and processed using the **Biopython** library, which provides tools for working with biological sequence data.

---

## Data Processing

After retrieving the sequences, two main analyses were performed:

1. **GC Content Analysis**

GC content measures the percentage of guanine (G) and cytosine (C) nucleotides in a DNA sequence. GC content is an important biological metric because it can influence DNA stability, gene expression, and evolutionary patterns.

For each sequence, GC content was calculated using Python and Biopython tools.

---

2. **Sequence Length Analysis**

The length of each DNA sequence was also calculated. Sequence length can vary depending on the specific mitochondrial region or gene that was retrieved.

Understanding sequence length distributions can help identify patterns in mitochondrial genome structure.

---

## Visualization

Two visualizations were generated using Python plotting libraries.

- A **histogram of GC content**
- A **histogram of sequence lengths**

These figures help illustrate how the values are distributed across the dataset.

Additionally, an **interactive visualization** was created using Plotly as part of the bonus challenge.

---

# Results

## GC Content Distribution

![GC Content Distribution](figure1.png)

Figure 1 shows the distribution of GC content values across the mitochondrial DNA sequences analyzed in this project.

Most sequences fall within a relatively narrow GC content range. This is expected because mitochondrial DNA typically has conserved nucleotide composition compared to nuclear DNA. The histogram demonstrates that GC content is relatively stable across the dataset.

---

## Sequence Length Distribution

![Sequence Length Distribution](figure2.png)

Figure 2 shows the distribution of sequence lengths across the dataset.

The variation in sequence length reflects differences between mitochondrial regions and genes that were retrieved from the database. Some sequences are shorter gene fragments, while others represent longer portions of the mitochondrial genome.

---

# Discussion

The results demonstrate how computational tools can quickly analyze biological sequence data. Using Python allowed automated processing of multiple sequences, which would be time-consuming to perform manually.

The GC content analysis showed that mitochondrial sequences generally maintain a consistent nucleotide composition. This reflects the evolutionary constraints placed on mitochondrial genes, which are essential for cellular energy production.

The sequence length distribution also highlights the diversity of mitochondrial gene fragments available in biological databases.

Overall, this project demonstrates the power of combining biological databases with programming tools to perform reproducible and scalable analyses.

---

# Conclusion

In this project, mitochondrial DNA sequences were retrieved from the NCBI database and analyzed using Python and Biopython.

Two primary analyses were conducted:
- GC content analysis
- Sequence length analysis

The results were visualized using histograms and an additional interactive plot. These analyses provide insight into sequence composition and demonstrate how computational approaches can be used to study biological data.

This workflow illustrates how bioinformatics tools can be used to retrieve, analyze, and visualize biological sequence data efficiently.

---

# Interactive Visualization (Bonus)

An additional interactive visualization was created using Plotly.

The interactive plot allows users to:

- Hover over data points
- Zoom into regions of the plot
- Explore sequence statistics dynamically

The interactive file included in this repository is: interactive_plot.html


Opening this file in a web browser allows full interaction with the visualization.

---

# Summary of Project Files

- `final_analysis.py` — Main Python analysis script  
- `interactive_plot.py` — Script used to generate the interactive visualization  
- `data.csv` — Processed dataset used for plotting  
- `figure1.png` — GC content histogram  
- `figure2.png` — Sequence length histogram  
- `interactive_plot.html` — Interactive visualization  
- `README.md` — Project documentation  
- `analysis_report.md` — Analysis report
