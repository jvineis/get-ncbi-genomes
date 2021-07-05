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
    
# Now you can change into the directory where all of the MAGs ended up and run the script that will generate and anvio db, run HMMs for single copy genes which allow for the generation of simple summary statistics for each MAG including completion scores and the probability that the MAG represents a candidate phyla.

    cd BAKER/
    ls *gz | cut -f 1,2,3 -d _ > sample-names.txt
    conda activate anvio-6.2
    sbatch x_gen-contigsdb.shx
    
# Next you will want to run the anvio command that will return summary statistics for each of your MAGs in a single table. But first you will need to build an externa genomes txt file.  The steps for this process are outlined below.

    ls *.db | sed 's/\.db//g' | sed 's/\./_/g' > 1
    ls *.db > 2
    paste 1 2 > external-genomes.txt
    
#### add the text below to the top of the external-genomes.txt file

    name	contigs_db_path
    
#### run the command to summarize the MAGs
   
    sbatch x_get-genome-summaries.shx

# Once this porcess is complete, you might want to run the gtdbtk taxonomy caller as outlined by the steps below including 1) build a file that contains the path and name for each MAG required by gtdbtk 2) run the gtdbtk pipeline. 

    conda deactivate 
    conda activate gtdbtk
    ls *.fna | grep -v genomic > 1
    ls *.fna | grep -v genomic | sed 's/\.fna//g' > 2
    paste 1 2 > x_gtdb-batchfile.txt
    sbatch x_run-gtdbtk.shx
    
## Now you may want to incorportate these MAGs into an existing set of MAGs that you have already run a similar set of bioinformatic steps on.  I will outline the steps below to combine the MAGs in the analysis that you conucted above with another set of MAGs (with anvio dbs and single copy gene collections etc) into a single directory, and conduct a phylogenomic analysis using anvio.  

    rsync -HalP *.db /scratch/vineis.j/ESTUARY-and-FTR/
    cd rsync -HalP *.fna /scratch/vineis.j/ESTUARY-and-FTR/
    
    
    
    
    
    
    
    


