# get-ncbi-genomes
A tutorial that details how to download a list of genomes contained in the ncbi database

# TO GET NCBI LIST OF GENOMES
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt
mv assembly_summary.txt bacterial-assembly.txt
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/assembly_summary.txt
mv assembly_summary.txt archaeal-assembly.txt
cat bacterial-assembly.txt archaeal-assembly.txt > complete-ncbi-genomes-summary.txt
