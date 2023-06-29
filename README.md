# PDB Viewer for Research

Performs blast search and merge with PDB files, rendering web pages, etc


1. small_polypeptide
Create a list of all known protein-peptide complexes. Use the REST API to examine the annotation for each PDB ID and identify those with multiple entries containing polypeptide molecules with a length of 50 or less, which can be considered protein-peptide complexes.
 
 
 2. BLAST search with local DB
 Create a BLAST database from protein and peptide pdb files in protein and peptide directories, respectively, and perform BLAST search by installing BLAST, generating local DB, and converting pdb files to fasta format using pdb_tools, and display sequence list and file names (PDBIDs) in the BLAST search results.
 
 3. PDB_MERGE
Merge protein and peptide PDB files based on PDBID and chain information from Pepbind_list file, and store the resulting complex PDB files in the "complex" directory for later use in training. PDB merge from pdb_tools will be used for merging.

 4. 3Dmol-renderer
 Create a web page using Node.js and 3Dmol.js to visualize each complex 
