Structure Based Drug Design and Struture Based Virtual Screening

Here we are going to use open source software to do all the works. These following works can be done using commercial softwares i.e. Schrodinger suites (Maestro)

Protein Structure Preparation 
    
    Fix common problems
    
        -Tautomer (Molprobity), pH (Propka), protonation (Avogadro, openbabel, AutoDock)
        
        - Missing side chains (SwissPDB Viewer)
        
        - Missing Loops (SwissPDB Viewer)
    
    Remove unwanted molecules
    
        - Counterions, artifacts, of crystallography, waters
    
    Optimize your Strcuture
    
        - Hydrogen-bond Otimization
        
        - Remove water
        
        - Restrained minimization

##### Good CADD starts with good science. Have a good understanding about the following: #####

* Srcuture Quality

* Conformantional State

* Experimental Design


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
    
    
