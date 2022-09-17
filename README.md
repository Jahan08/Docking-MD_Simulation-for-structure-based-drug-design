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


# Docking Tutorial Udemy (AutoDock4) (seperate file uploaded for this)

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

### Note - Sometimes, MGLTOOLS can show errors, Protein structure downloaded from PDB can show these errors. To get rid of that prepare the protein structure with Modeller first

* Assume receptor is rigid
* Assumes ligand is flexible

Ensemble of receptor-ligand poses produced by docking, which can be  ranked by score. More negative score is better. 

Scoring Functions:
* do not correlate with IC50, EC50, Kd etc
* do not provide a rank-ordering of ligands
* are optimized to give good enrichment
    * separates "good" ideas from "bad"
    * Limit the number of ligands to be investigated further
    
## Important Steps for Molecular Docking

  #### Step-1 Selection of 3D structure of protein (Download the 3D strcuture from UNIPROT/PDB (X-ray crystallography, NMR, cryo-EM) -> Predict the 3D structure (homology modeling, I-tasser, Alpha-Fold))

### Homology Modeling (Predict 3D structure of protein)

Homology modeling, also known as comparative modeling of protein, refers to constructing an atomic-resolution model of the "target" protein from its amino acid sequence and an experimental three-dimensional structure of a related homologous protein (the "template")
Homology modeling relies on the identification of one or more known protein structures likely to resemble the structure of the query sequence, and on the production of an alignment that maps residues in the query sequence to residues in the template sequence.


### Homology Modelling using Modeller



Emboss-Needle

I-Tasser

Alpha-fold

Pro-Check

  #### Step-2 Preparation of protein structure for docking (Check protein Structure with Emboss Needle and then repair the structure with Modeller script)
  
  The structure we used has ligand with it.We can load .pdb into mgltools, remove water(edit -> delete water), remove unnecessary part(go to protein left side and to the bottom and select them edit -> Deletedelete selected atoms), missing atoms can be checked(edit-misc-missing atom ->repair missing atom), add charges(edit-charge-kollman charges) and after that check charges and any residue mentioned in the list will be selected (equally distributed charges through out the protein), Save(grid -> macromolecule -> select the protein  -> ok -> save the protein as .pdbqt file)
  
  #### Step-3 Ligand Preparation 
  
  Ligand structure(Can be cocrystallized with the protein, download 3D structure from PubChem, Zinc15, the Cambridge structural database ) or drawing(chemdoodle and saved as .mol file and convert it to 3D structure with open-babel(installed) and iBabel(add the path of open-babel and save ligand as .mol2 file format)—then minimize and optimize the structure in Avogadro—convert the ligand.mol2 to .pdbqt through open-babel for docking)Ligand preparation
  
  #### Step-4 Defining Active Sites
  
  Blind docking(whole protein surface has been used to find the active sites) or specific docking (particular area would be specified—from literature or prediction of binding site)
  To find the ligand binding residues of the protein-article or coach server(take 10 hours) ->upload the fasta sequence and protein.pdb structure and provide academic email to find the binding sites residues—specific docking and otherwise blind docking
  
  #### Step-5 Docking protocol setup
  
Go to left side receptor click + and will see all the residues where you can select the binding sites residuesafter selecting the binding sites residues select GRID and we change the value in 3 direction of the grid box

In the case of blind docking grid box will cover the whole protein

  ##### Setting parameters for docking (define scoring and sampling algorithm)(autodock or autodock vina is better)

# Virtual Screening with AutoDock Vina

In the uplaoded jupyter notebook (Docking_with_autodock.ipynb) I have shown how to use AutoDock to dock single ligand to our target protein. in the following I will show how to use Autodock vina to dock a ligand library:   

##### Before conduct docking on vina, we have to prepare configuration file
Receptor = receptor.pdbqt
Ligand = ligand.pdbqt
Out = out.pdbqt
center_x = X center (from grid box information)
center_y = Y center (from grid box information)
center_z = Z center (from grid box information)
size_x = number of points in x dimension
size_y = number of points in y dimension
size_z = number of points in z dimension
exhaustiveness = 8 (high is good)---save this as conf in the desired folder)

##### use terminal to run vina with following command
"~/autodock_vina_1_1_2_mac_catalina_64bit/bin/vina.exe"(path of vina executable) --config conf.txt(configuration file) --log log.txt(output file)

##### Note - Copy conf.txt, vina.exe, ligand.pdbqt, protein.pdbqt files into a separate folder

##### Run the following command 

 vina.exe –-config conf.txt –-log log.txt 

##### After running docking on vina we will visualize that on autodock
Load ligand -> Analyze -> docking -> docking results from autovina -> ouput -> multiple 
Conformations
Load protein -> Analyze -> macromolecule -> receptor.pdbqt file
Pressing right directed arrow we can see different conformations


    
