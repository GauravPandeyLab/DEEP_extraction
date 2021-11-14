# Data-driven ExposurE Profile (DEEP) extraction
## Discovering air toxic mixture leading to asthma outcome by machine learning


DEEP uses XGBoost algorithm to identify air toxic combinations associated with health outcomes. The combinations identified using XGBoost were then adjusted for potential confounders to identify early-life multi-air toxic combinations, statistical interactions within combinations. Our approach identified several combinations of air toxics associated with asthma in [Y.C.Li et al.](https://www.jci.org/articles/view/152088). 

Full citation: 

Li YC, Hsu HL, Chun Y, Chiu PH, Arditi Z, Claudio L, Pandey G, Bunyavanich S. Machine learning-driven identification of early-life air toxic combinations associated with childhood asthma outcomes. J Clin Invest. 2021 Oct 5:e152088. doi: 10.1172/JCI152088. Epub ahead of print. PMID: 34609967.

## Required Packages
    
    python==3.7.4
    scikit-learn==0.22
    xgboost==1.2.0
    numpy==1.19.5
    pandas==0.25.3
    scipy==1.3.1
    statsmodels==0.10.1
    matplotlib==3.1.0
    pydotplus==2.0.2
    argparse==1.1

In addition to generate the figure used in our paper, the following R packages are required:
    
    sas7bdat==0.5
    metaviz==0.3.1

## Usage

Step 0: Prepare your data in csv under `data` directory, the example of data format is provided in this repository.
    
Step 1: Applying DEEP to the desired outcome(s), the results will be generated to `result_dir` (default = ./result).
    
    python deep_main.py --filename [outcome.csv] --outcome [outcome]
    

Parameters of deep_main.py

      -h, --help            show this help message and exit
      --outcome OUTCOME, -o OUTCOME
                            Name of outcome
      --filename FILENAME, -p FILENAME
                            Path of csv data
      --binary_outcome BINARY_OUTCOME, -b BINARY_OUTCOME
                            True if the outcome is labeled in binary, default=True
      --result_dir RESULT_DIR, -r RESULT_DIR
                            desired result directory prefix, default="./result"
      --num_tree_print NUM_TREE_PRINT, -ntp NUM_TREE_PRINT
                            Number of trees for each path printed to result
                            directory, default = -1 implies printing all of them

    
Step 2: Merging all the result files from multiple outcomes, and then performing the FDR correction

    python merge_multiple_outcomes.py --result_dir [result_directory]
    
Printing Figure 2 & 3 (Table of False discovery rate (FDR), Odds ratios (OR) of individual pollutants and combinations which are significantly associated to the outcomes):

    python profile_table.py --result_dir [result_directory]
    


Taking the sample data as example, the whole pipeline will be:

    python deep_main.py --filename DailyControllerMedication.csv --outcome DailyControllerMedication
    python deep_main.py --filename EmergencyRoomVisit.csv --outcome EmergencyRoomVisit
    python deep_main.py --filename OvernightHospitalization.csv --outcome OvernightHospitalization
    python merge_multiple_outcomes.py --result_dir ./result
    python profile_table.py --result_dir ./result
    
    
Result:
    
## Sample Data

Due to IRB constraints, we are unable to publicly share the asthma cohort dataset used in our study. Thus, as sample data to test our code, we are providing a randomized dataset based on the original data distribution in this repository. We included the results generated by the randomized data in `result` directory.

## Pipeline Summary

* In the `deep_main.py` script, it performs the DEEP extraction on single health outcome, including: 
** Frequent profile extraction via 100 runs of XGBoost
** Statistical assessment of the frequent profiles with potential confounders. 

* After running DEEP on the multiple health outcomes, `merge_multiple_outcomes.py` merges the results into 1 and performs the FDR correction. 
* `profile_table.py` filters out the individual air toxic and combination of air toxic which are positively associated with the health outcome. `profile_table.py` also calls `Rscript\profile_table.R` to visualize the result, as the figure 2 and 3 in our article.


## Contact
In case of issues with the code, please let us know through the Issues functionality and/or contact Yan-Chak Li [yan-chak.li@mssm.edu](mailto:yan-chak.li@mssm.edu) and Gaurav Pandey [gaurav.pandey@mssm.edu](mailto:gaurav.pandey@mssm.edu).

