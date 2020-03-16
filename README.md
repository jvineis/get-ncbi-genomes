# TO GET NCBI LIST OF GENOMES
    
    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt
    mv assembly_summary.txt bacterial-assembly.txt
    wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/assembly_summary.txt
    mv assembly_summary.txt archaeal-assembly.txt
    cat bacterial-assembly.txt archaeal-assembly.txt > complete-ncbi-genomes-summary.txt

# COLLECT THE IDs FOR THE TARGET GENOMES THAT YOU WANT.

    grep Chlorobium complete-ncbi-genomes-summary.txt | cut -f 20 > Chlorobium-ncbi-genome-names.txt

# Generate a bash script that contains a wget command for each of the genomes in your list. 
 
    python gen-ncbi-wget-commands.py Chlorobium-ncbi-genome-names.txt Chlorobium-ncbi-command.shx
 
# Run the bash command. 

    bash Chlorobium-ncbi-command.shx


