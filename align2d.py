from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='4uum', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4uumA', atom_files='4uum.pdb')
aln.append(file='TvLDH.ali', align_codes='TvLDH')
aln.align2d(max_gap_length=50)
aln.write(file='TvLDH-4uumA.ali', alignment_format='PIR')
aln.write(file='TvLDH-4uumA.pap', alignment_format='PAP')
