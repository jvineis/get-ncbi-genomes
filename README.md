# TO GET NCBI LIST OF GENOMES
    
    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt
    mv assembly_summary.txt bacterial-assembly.txt
    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/assembly_summary.txt
    mv assembly_summary.txt archaeal-assembly.txt
    cat bacterial-assembly.txt archaeal-assembly.txt > complete-ncbi-genomes-summary.txt

# COLLECT THE IDs FOR THE TARGET GENOMES THAT YOU WANT.

    grep Chlorobium complete-ncbi-genomes-summary.txt | cut -f 20 > Chlorobium-ncbi-genome-names.txt

# Download each	of the genomes.
    
    for next in `cat complete-genome-list.txt`; do wget -P /Users/joevineis/ncbi_genome_db/ "$next"/*genomic.fna.gz; done


