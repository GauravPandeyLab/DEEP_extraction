import sys
import os

suffix = sys.argv[-1]
outcome_binary_dict = {
    'resampled_daily_controller_past6months': True,
    'resampled_emergency_dept': True,
    'resampled_hospitalize_overnight': True,
}

for outcome in outcome_binary_dict:
    lsf_str = "#!/bin/bash\n#BSUB -J asthma_project\n#BSUB -P acc_pandeg01a\n#BSUB -q express\n" \
              "#BSUB -n 4\n#BSUB -W 2:00\n#BSUB -o analyzer_%J.stdout\n#BSUB -eo analyzer_%J.stderr\n" \
              "#BSUB -R rusage[mem=10000]\nmodule purge\n"
    outcome_replaced = outcome.replace('(', '\(').replace(')', '\)')
    python_cmd = "python deep_main.py --filename {}.csv --outcome {}".format(outcome, outcome)

    lsf_name = "{}.lsf".format(outcome)
    lsf_replaced_name = "{}.lsf".format(outcome_replaced)
    script = open(lsf_name, 'w')
    script.write(lsf_str)
    script.write(python_cmd)
    script.close()
    os.system("bsub < {}".format(lsf_replaced_name))
    os.remove(lsf_name)