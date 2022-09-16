# Structure Based Drug Design and Struture Based Virtual Screening

Structure-based drug design (SBDD) is the design and optimisation of a hit or lead compound using structural information of target protein obtained from either X-ray crystallography, cryo-EM or NMR

Structure based drug design is the workhorse of CADD (computer aided drug design)
With that we can:
 * Predict druggability
 * Identify ligand binding sites
 * Virtual screen for novel chemical matter
 * Optimize potency of leads
 * Reduce off-target effects


Here we are going to use open source software to do all the works. Which can be done using commercial softwares i.e. Schrodinger suites (Maestro)

# Good CADD starts with good science. Have a good understanding about the following: 

* Sructure Quality

* Conformantional State

* Experimental Design


# Docking Tutorial Udemy

## Docking Types
   * Rigid (both protein and ligand)
   * Flexible (both protein and ligand)
   * Constrained (protein is constrained)
   
## Algorithm types 
   * Sampling Algorithm - Samples the conformations of ligand in the binding site/s
   * Scoring Algorithm - Measures the binding energy of all poses of the ligand (only accounts for non-bonded interactions(electrostatic interactions, Hydrogen Bonds, Salt bridges, van der Waals interactions))
   
## There are six sampling algorithms
   * Shape complementary (PatchDock)
   * Genetic Sampling Algorithm (AutoDock4)
   * Force Field algorithm 
   * Empirical Scoring function
   * Knowledge based scoring function
   * Consensus-based scoring function

### During Docking 

* Assume receptor is rigid
* Assumes ligand is flexible

Ensemble of receptor-ligand poses produced by docking, which can be  ranked by score. More negative score is better. 

Scoring Functions:
* do not correlate with IC50, EC50, Kd etc
* do not provide a rank-ordering of ligands
* are optimized to give good enrichment
    * separates "good" ideas from "bad"
    * Limit the number of ligands to be investigated further
    
   
# Virtual Screening with AutoDock Vina

In the uplaoded jupyter notebook (Docking_with_autodock.ipynb) I have shown how to use AutoDock to dock single ligand to our target protein. in the following I will show how to use Autodock vina to dock a ligand library:    
    
