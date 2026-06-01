# Template Index

This index maps the repository's Stata templates to common empirical research tasks. Use it to find the closest starting point, then adapt variable names, paths, controls, and model assumptions to your project.

## Method Taxonomy

| Category | Typical use |
| --- | --- |
| Data management | Importing, cleaning, reshaping, grouping, imputing, winsorizing, and preparing panel data |
| Descriptive and correlation analysis | Summary statistics, correlation tables, reliability checks, and multicollinearity checks |
| Basic regression | Baseline regressions, fixed effects models, and interactive fixed effects |
| Endogeneity and IV | Instrumental variables, breakpoint/RDD-style workflows, and endogeneity checks |
| Robustness and heterogeneity | Robustness checks, placebo tests, parallel trends, subgroup analysis, and heterogeneity analysis |
| Mechanism analysis | Mediation, moderating effects, and non-parametric mechanism analysis |
| Advanced models | PSM-DID, synthetic control, PCA/factor analysis, entropy method, time series, and clustering |
| Export and utilities | Table export, loops, one-click workflows, fake data, and project-specific utility snippets |

## 01 Data Management

| Template | Use case |
| --- | --- |
| [`AI_generated_data.md`](../01_Data_Management/AI_generated_data.md) | Generate or structure example data for workflow testing |
| [`Calculate_deflator.md`](../01_Data_Management/Calculate_deflator.md) | Calculate deflators or adjusted economic indicators |
| [`Clean_-_merge_strings_in_multiple_cells.md`](../01_Data_Management/Clean_-_merge_strings_in_multiple_cells.md) | Clean and merge string values across cells or observations |
| [`Cleaning-other.md`](../01_Data_Management/Cleaning-other.md) | Miscellaneous data cleaning operations |
| [`Generate_new_groups_based_on_conditions_+_report_counts_by_group.md`](../01_Data_Management/Generate_new_groups_based_on_conditions_+_report_counts_by_group.md) | Generate groups from conditions and report group counts |
| [`Group_samples.md`](../01_Data_Management/Group_samples.md) | Create grouped samples for downstream analysis |
| [`Import_and_export_data.md`](../01_Data_Management/Import_and_export_data.md) | Import and export data files |
| [`Loop_to_modify_variable_names.md`](../01_Data_Management/Loop_to_modify_variable_names.md) | Rename or transform variable names in loops |
| [`Missing_value_imputation.md`](../01_Data_Management/Missing_value_imputation.md) | Fill, interpolate, or impute missing values |
| [`Multiple_stock_codes.md`](../01_Data_Management/Multiple_stock_codes.md) | Handle records with multiple stock codes |
| [`Null_value_handling.md`](../01_Data_Management/Null_value_handling.md) | Detect and handle null or missing-like values |
| [`Panel_data_extended_for_one_year.md`](../01_Data_Management/Panel_data_extended_for_one_year.md) | Extend panel data by one time period |
| [`Panel_data_transformation.md`](../01_Data_Management/Panel_data_transformation.md) | Transform data into panel-ready structure |
| [`Quantile_regression.md`](../01_Data_Management/Quantile_regression.md) | Quantile regression snippet currently stored in data management |
| [`Ranking.md`](../01_Data_Management/Ranking.md) | Generate rankings or ranked groups |
| [`The_variable_takes_the_30th_percentile.md`](../01_Data_Management/The_variable_takes_the_30th_percentile.md) | Extract percentile-based variable thresholds |
| [`Variable_category_conversion.md`](../01_Data_Management/Variable_category_conversion.md) | Convert categorical variables |
| [`Winsorization.md`](../01_Data_Management/Winsorization.md) | Winsorize variables at chosen cutoffs |
| [`date.md`](../01_Data_Management/date.md) | Parse or transform date variables |
| [`length-width_transformation.md`](../01_Data_Management/length-width_transformation.md) | Reshape data between wide and long forms |
| [`vertical_merger.md`](../01_Data_Management/vertical_merger.md) | Append or vertically merge datasets |

## 02 Descriptive and Correlation

| Template | Use case |
| --- | --- |
| [`Correlation_analysis_and_export.md`](../02_Descriptive_and_Correlation/Correlation_analysis_and_export.md) | Correlation analysis and export |
| [`Descriptive_statistics.md`](../02_Descriptive_and_Correlation/Descriptive_statistics.md) | Summary statistics table generation |
| [`Multicollinearity_test.md`](../02_Descriptive_and_Correlation/Multicollinearity_test.md) | Variance inflation factor and multicollinearity checks |
| [`Related_analysis_export.md`](../02_Descriptive_and_Correlation/Related_analysis_export.md) | Export related or correlation analysis results |
| [`Reliability_analysis.md`](../02_Descriptive_and_Correlation/Reliability_analysis.md) | Reliability or consistency analysis |

## 03 Basic Regression

| Template | Use case |
| --- | --- |
| [`baseline_regression.md`](../03_Basic_Regression/baseline_regression.md) | Baseline panel regression and regression table export |
| [`Interactive_fixed_effects.md`](../03_Basic_Regression/Interactive_fixed_effects.md) | Interactive fixed effects model setup |

## 04 Endogeneity and IV

| Template | Use case |
| --- | --- |
| [`Breakpoint_regression_and_instrumental_variable_regression.md`](../04_Endogeneity_and_IV/Breakpoint_regression_and_instrumental_variable_regression.md) | Breakpoint/RDD-style regression and instrumental variable workflows |

## 05 Robustness and Heterogeneity

| Template | Use case |
| --- | --- |
| [`Heterogeneity_analysis.md`](../05_Robustness_and_Heterogeneity/Heterogeneity_analysis.md) | Grouped heterogeneity analysis |
| [`Parallel_trend_test.md`](../05_Robustness_and_Heterogeneity/Parallel_trend_test.md) | Parallel trend checks for DID-style designs |
| [`Robustness_check.md`](../05_Robustness_and_Heterogeneity/Robustness_check.md) | Robustness checks with alternative variables or specifications |
| [`heterogeneity.md`](../05_Robustness_and_Heterogeneity/heterogeneity.md) | Additional heterogeneity analysis snippet |
| [`placebo_test.md`](../05_Robustness_and_Heterogeneity/placebo_test.md) | Placebo tests and randomization-style checks |

## 06 Mechanism Analysis

| Template | Use case |
| --- | --- |
| [`Non-parametric_mechanism_analysis.md`](../06_Mechanism_Analysis/Non-parametric_mechanism_analysis.md) | Non-parametric mechanism or mediation analysis |
| [`intermediary.md`](../06_Mechanism_Analysis/intermediary.md) | Mediation or intermediary effect analysis |

## 07 Advanced Models

| Template | Use case |
| --- | --- |
| [`PSM-DID.md`](../07_Advanced_Models/PSM-DID.md) | Propensity score matching combined with DID |
| [`Principal_component_analysis_factor_analysis.md`](../07_Advanced_Models/Principal_component_analysis_factor_analysis.md) | PCA and factor analysis |
| [`Synthetic_Control_SCM.md`](../07_Advanced_Models/Synthetic_Control_SCM.md) | Synthetic control method examples |
| [`Technological_innovation_efficiency-malmq2.md`](../07_Advanced_Models/Technological_innovation_efficiency-malmq2.md) | Malmquist productivity or innovation efficiency workflow |
| [`Time_series_code_learning.md`](../07_Advanced_Models/Time_series_code_learning.md) | Time-series analysis snippets |
| [`cluster_analysis.md`](../07_Advanced_Models/cluster_analysis.md) | Cluster analysis |
| [`entropy_method.md`](../07_Advanced_Models/entropy_method.md) | Entropy method for index construction |

## 08 Export and Utilities

| Template | Use case |
| --- | --- |
| [`99_difficult_and_complicated_diseases.md`](../08_Export_and_Utilities/99_difficult_and_complicated_diseases.md) | Miscellaneous troubleshooting snippets |
| [`City_statistical_yearbook_processing.md`](../08_Export_and_Utilities/City_statistical_yearbook_processing.md) | City statistical yearbook processing |
| [`Code_tips.md`](../08_Export_and_Utilities/Code_tips.md) | General Stata code tips |
| [`Digital_Economy_Digital_Inclusive_Finance.md`](../08_Export_and_Utilities/Digital_Economy_Digital_Inclusive_Finance.md) | Digital economy and digital inclusive finance workflow |
| [`Generate_various_variables_as_required.md`](../08_Export_and_Utilities/Generate_various_variables_as_required.md) | Generate variables for common empirical needs |
| [`full_set.md`](../08_Export_and_Utilities/full_set.md) | Full empirical workflow example |
| [`generate_fake_data.md`](../08_Export_and_Utilities/generate_fake_data.md) | Generate fake or simulated data |
| [`oneclick.md`](../08_Export_and_Utilities/oneclick.md) | One-click or automated variable selection workflow |
| [`various_loops.md`](../08_Export_and_Utilities/various_loops.md) | Common loop patterns and automation snippets |

## Notes for Users

- Templates are starting points, not complete research designs.
- Replace file paths, variable names, panel identifiers, and controls before running the code.
- Check whether a template depends on community-contributed Stata commands such as `reghdfe`, `winsor2`, `psmatch2`, `esttab`, `outreg2`, or `reg2docx`.
- When in doubt, start from the simplest baseline template and add complexity step by step.
