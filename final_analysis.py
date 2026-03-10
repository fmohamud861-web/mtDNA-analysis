#!/usr/bin/env python3

"""
This script retrieves human mitochondrial DNA sequences from the NCBI database
using the Entrez API. It calculates GC content and sequence length and
generates visualizations of the results.
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import time


# Retrieve sequence IDs
def get_sequence_ids():

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    params = {
        "db": "nuccore",
        "term": "human mitochondrial DNA AND Homo sapiens",
        "retmax": 100,
        "retmode": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["esearchresult"]["idlist"]


# Fetch sequences
def fetch_sequences(ids):

    sequences = []

    for seq_id in ids:

        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

        params = {
            "db": "nuccore",
            "id": seq_id,
            "rettype": "fasta",
            "retmode": "text"
        }

        r = requests.get(fetch_url, params=params)
        fasta = r.text

        lines = fasta.split("\n")
        sequence = "".join(lines[1:])

        if sequence:
            sequences.append(sequence)

        time.sleep(0.4)

    return sequences


# Analyze sequences
def analyze_sequences(sequences):

    lengths = []
    gc_values = []

    for seq in sequences:

        lengths.append(len(seq))

        gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
        gc_values.append(gc)

    df = pd.DataFrame({
        "sequence_length": lengths,
        "gc_content": gc_values
    })

    df.to_csv("data.csv", index=False)

    return df


# Create plots
def create_plots(df):

    plt.hist(df["gc_content"], bins=20)
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Frequency")
    plt.savefig("figure1.png")
    plt.clf()

    plt.hist(df["sequence_length"], bins=20)
    plt.title("Sequence Length Distribution")
    plt.xlabel("Sequence Length")
    plt.ylabel("Frequency")
    plt.savefig("figure2.png")


def main():

    print("Getting sequence IDs...")
    ids = get_sequence_ids()

    print("Downloading sequences...")
    sequences = fetch_sequences(ids)

    print("Sequences retrieved:", len(sequences))

    print("Analyzing sequences...")
    df = analyze_sequences(sequences)

    print("Generating plots...")
    create_plots(df)

    print("Analysis complete!")


if __name__ == "__main__":
    main()
