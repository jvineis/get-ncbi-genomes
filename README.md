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

### A example of how to obtain MAGs from NCBI and use anvio to generate descriptive statistics and phylogenomics. The MAGs used in this example are derived from the Brett Baker et. al. mscript https://microbiomejournal.biomedcentral.com/track/pdf/10.1186/s40168-015-0077-6.pdf

# In this manuscript, you will find an NCBI project id (PRJNA270657) that is linked to the MAGs. You can pull out the paths to the MAGs in the NCBI server using a simple grep command and generate a single bash script to download all the associated MAGs as above. Here are the commands that I used to do this.

    grep PRJNA270657 assembly_summary.txt | cut -f 20 > Baker-mag-genome-names.txt
    python gen-ncbi-wget-commands.py Baker-mag-genome-names.txt Baker-ncbi-command.shx
    sbatch Baker-ncbi-command.shx
    
# Now you can change into the directory where all of the MAGs ended up and run the script that will generate and anvio db, run HMMs for single copy genes and generate simple summary statistics for each MAG.

    cd BAKER/
    ls *gz | cut -f 1,2,3 -d _ > sample-names.txt
    conda activate anvio-6.2
    sbatch x_gen-contigsdb.shx
    

