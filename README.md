# get-ncbi-genomes
A tutorial that details how to download a list of genomes contained in the ncbi database

### 1. First you need a list of all the genomes contained at NCBI. Run the command below in the terminal
##### Collect the list of archeal genomes from NCBI
    
    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/archaea_assembly_summary.txt

##### Collect the list of bacterial genomes from NCBI

    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/bacteria_assembly_summary.txt

### 2. Create a list of only the complete genomes from each of the lists.

    grep "Complete" archaea_assembly_summary.txt > archaea-complete.txt
    grep "Complete" bacteria_assembly_summary.txt > bacterial-complete.txt

### 3. Concatenate the list of genomes

    cat archaea-complete.txt bacterial-complete.txt > archaea-bacterial-complete-list.txt

### 4. Get the genome ids

    cut -f 20 archaea-bacterial-complete-list.txt > complete-genome-list.txt

### 5. Download the targeted genomes

    for next in `cat complete-genome-list.txt`; do wget -P /Users/joevineis/ncbi_genome_db/ "$next"/*genomic.fna.gz; done
