# Structure Based Drug Design and Struture Based Virtual Screening

Structure-based drug design (SBDD) is the design and optimisation of a hit or lead compound using structural information of target protein obtained from either X-ray crystallography, cryo-EM or NMR

Here we are going to use open source software to do all the works. Which can be done using commercial softwares i.e. Schrodinger suites (Maestro)

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

      # here I am gonna show how to use modeller to correct the protein structureby using three python script:


# DOCKING (AutoDock, AutoDock Vina) #####

* Assume receptor is rigid
* Assumes ligand is flexible

Ensemble of receptor-ligand poses produced by docking, which can be  ranked by score. More negative score is better. 

high-throughput virtual screens have suffered from quality issues, and because of this, the docking score that is output from a virtual screen should in no way be used as a metric to compare with ligand affinities.

Recent findings from the Shoichet lab using ultra-large docking libraries suggest that some of the quality issues that have plagued high throughput virtual screening in the past may be partially resolved with the screening of more compounds that cover more of chemical space. This is because it is now possible to dock libraries of compounds with over 100 million ligands in a reasonable amount of time, and thus screen more of chemical space.


Scoring Functions:
* do not correlate with IC50, EC50, Kd etc
* do not provide a rank-ordering of ligands
* are optimized to give good enrichment
    * separates "good" ideas from "bad"
    * Limit the number of ligands to be investigated further
    
    
# WorkFlow for Virtual Screening:

Compund Library Preparation (Obtain Compound Library -> Filter Library -> LigPrep Library).   ''''   -> Virtual Screening -> Post Processing 
Receptor Grid Preparation (Prepare Protein -> Generate Grids -> Test Grids)                   ''''                                 
    
Post Processing -> Compile Virtaul Screening Results -> First Cut -> Secondary Scoring -> Second Cut -> Visual Inspection/Voting -> Final Cut -> Generate Buy List    
    
                            
