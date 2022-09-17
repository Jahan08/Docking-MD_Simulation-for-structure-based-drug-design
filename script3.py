from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

class MyModel(AutoModel):
    def select_atoms(self):
        return Selection(self.residue_range('133:A', '135:A'),
                         self.residue_range('217:A', '230:A'))

a = MyModel(env, alnfile = 'alignment.ali',
            knowns = 'qpdb', sequence = 'qpdb_fill')
a.starting_model= 1
a.ending_model  = 1

a.make()