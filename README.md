# Structure Based Drug Design and Struture Based Virtual Screening

Structure-based drug design (SBDD) is the design and optimisation of a hit or lead compound using structural information of target protein obtained from either X-ray crystallography, cryo-EM or NMR

Here we are going to use open source software to do all the works. Which can be done using commercial softwares i.e. Schrodinger suites (Maestro)

# Good CADD starts with good science. Have a good understanding about the following: 

* Sructure Quality

* Conformantional State

* Experimental Design

# DOCKING (AutoDock, AutoDock Vina) #####

* Assume receptor is rigid
* Assumes ligand is flexible

Ensemble of receptor-ligand poses produced by docking, which can be  ranked by score. More negative score is better. 

Scoring Functions:
* do not correlate with IC50, EC50, Kd etc
* do not provide a rank-ordering of ligands
* are optimized to give good enrichment
    * separates "good" ideas from "bad"
    * Limit the number of ligands to be investigated further
    
In the uplaoded jupyter notebook (Docking_with_autodock.ipynb) I have shown how to use AutoDock to dock single ligand to our target protein. in the following I will show how to use Autodock vina to dock a ligand library:    
    
