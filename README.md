# Data-driven ExposurE Profile (DEEP) extraction - Discovering air toxic mixture leading to asthma outcome by machine learning

DEEP uses XGBoost algorithm to identify air toxic combinations associated with health outcomes. The combinations identified using XGBoost were then adjusted for potential confounders to identify early-life multi-air toxic combinations, statistical interactions within combinations. Our approach identified several combinations of air toxics associated with asthma in [Y.C.Li et al.](https://www.jci.org/articles/view/152088). 

## Required Packages

## Usage
Step 1: Applying DEEP to the desired outcome(s).
    
    python deep_main.py --filename [outcome.csv] --outcome [outcome]
    
Step 2: Merging all the result files from multiple outcomes, and then performing the FDR correction

    python merge_multiple_outcomes.py --result_dir [result_directory]
    
## Sample Data

## DEEP Summary

## Contact
In case of issues with the code, please let us know through the Issues functionality and/or contact Yan-Chak Li [yan-chak.li@mssm.edu](mailto:yan-chak.li@mssm.edu) and Gaurav Pandey [gaurav.pandey@mssm.edu](mailto:gaurav.pandey@mssm.edu).

