# 📊 Stata Empirical Research Templates

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Stata Version](https://img.shields.io/badge/Stata-15%2B-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

A comprehensive, ready-to-use collection of Stata code templates for empirical economics, finance, and social sciences. 

This repository provides full-pipeline code snippets covering everything from basic data management and descriptive statistics to advanced causal inference models (PSM-DID, RDD, SCM) and spatial econometrics. 

## 🎯 Project Scope

This project is designed for researchers, students, and analysts who use Stata for empirical research and want reusable templates for common research workflows.

It focuses on practical, copy-paste friendly examples for:

* organizing and cleaning research data;
* running baseline and extended regression models;
* conducting robustness, heterogeneity, endogeneity, and mechanism checks;
* applying common empirical methods such as PSM-DID and synthetic control;
* exporting tables and automating repetitive Stata tasks.

This repository is **not** a compiled Stata package or a substitute for method-specific econometrics documentation. Users should adapt each template to their own data, research design, and reporting standards.

For the current maintenance direction, see [`ROADMAP.md`](ROADMAP.md).

## 📑 Repository Structure

The code is organized logically following a standard empirical research workflow:

* **`01_Data_Management/`** - Panel data setup, reshaping, missing value imputation, winsorizing, and string cleaning.
* **`02_Descriptive_and_Correlation/`** - Summary statistics, correlation matrices, reliability, and multicollinearity (VIF) tests.
* **`03_Basic_Regression/`** - OLS baseline, Fixed Effects (FE), and Interactive Fixed Effects.
* **`04_Endogeneity_and_IV/`** - Instrumental Variables (2SLS), GMM, and handling endogeneity.
* **`05_Robustness_and_Heterogeneity/`** - Placebo tests, parallel trend tests, Regression Discontinuity (RDD), PSM-DID, and Synthetic Control Method (SCM).
* **`06_Mechanism_Analysis/`** - Mediation analysis, moderating effects, and non-parametric mechanisms.
* **`07_Advanced_Models/`** - Spatial econometrics (SDM/SAR/SEM), PCA, Factor Analysis, Entropy method, and Cluster Analysis.
* **`08_Export_and_Utilities/`** - Quick results export (`esttab`, `outreg2`), data simulation, and automation tricks.

For a file-by-file map of available templates, see [`docs/TEMPLATE_INDEX.md`](docs/TEMPLATE_INDEX.md).

## 🚀 How to Use

All files are provided in Markdown (`.md`) format with `stata` code blocks. This makes it extremely easy to read the explanations directly on GitHub and copy-paste the code snippets into your Stata `.do` files.

1. Browse the folders to find the specific econometric method or data processing trick you need.
2. Copy the code block.
3. Replace the placeholder variable names (e.g., `y`, `x`, `Control_Variables`) with your actual dataset variables.

## 🤝 Contributing

Contributions are welcome! If you have a highly efficient Stata snippet or a new econometric model template, feel free to open a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingStataCode`)
3. Commit your Changes (`git commit -m 'Add some AmazingStataCode'`)
4. Push to the Branch (`git push origin feature/AmazingStataCode`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
