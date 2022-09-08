# Structure Based Drug Design and Struture Based Virtual Screening

Here we are going to use open source software to do all the works. These following works can be done using commercial softwares i.e. Schrodinger suites (Maestro)

# Good CADD starts with good science. Have a good understanding about the following: #####

* Sructure Quality

* Conformantional State

* Experimental Design

# Fixing protein structure

Experimeantally found 3D structures of proteins generally have --

* non-protein components
* Missing side chain
* Missing residues

Modeller or SwissPDB Viewer can be used to fix these issues.


#### DOCKING (AutoDock, AutoDock Vina) #####

* Assume receptor is rigid
* Assumes ligand is flexible

Ensemble of receptor-ligand poses produced by docking, which can be  ranked by score. More negative score is better. 

Scoring Functions:
* do not correlate with IC50, EC50, Kd etc
* do not provide a rank-ordering of ligands
* are optimized to give good enrichment
    * separates "good" ideas from "bad"
    * Limit the number of ligands to be investigated further
    
    
#### WorkFlow for Virtual Screening: #####

Compund Library Preparation (Obtain Compound Library -> Filter Library -> LigPrep Library).   ''''   -> Virtual Screening -> Post Processing 
Receptor Grid Preparation (Prepare Protein -> Generate Grids -> Test Grids)                   ''''                                 
    
Post Processing -> Compile Virtaul Screening Results -> First Cut -> Secondary Scoring -> Second Cut -> Visual Inspection/Voting -> Final Cut -> Generate Buy List    
    
                            
