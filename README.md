# 📊 Stata Empirical Research Templates

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Stata Version](https://img.shields.io/badge/Stata-15%2B-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

A comprehensive, ready-to-use collection of Stata code templates for empirical economics, finance, and social sciences. 

This repository provides full-pipeline code snippets covering everything from basic data management and descriptive statistics to advanced causal inference models (PSM-DID, RDD, SCM) and spatial econometrics. 

## Quick Links

- [Template index](docs/TEMPLATE_INDEX.md) - file-by-file map of available templates
- [Contribution guidelines](CONTRIBUTING.md) - how to add or improve a template
- [Roadmap](ROADMAP.md) - current maintenance direction
- [Maintenance audit](docs/MAINTENANCE_AUDIT.md) - repository status and maintenance gaps

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

1. Start from the [template index](docs/TEMPLATE_INDEX.md) or browse the workflow folders.
2. Open the template that matches your method or data task.
3. Copy the Stata code block into your `.do` file.
4. Replace placeholder variable names such as `y`, `x`, `controls`, `id`, and `time` with your project variables.
5. Check whether the template requires community-contributed commands such as `reghdfe`, `winsor2`, `psmatch2`, `esttab`, or `outreg2`.

## 🤝 Contributing

Contributions are welcome. Before opening a pull request, please read [`CONTRIBUTING.md`](CONTRIBUTING.md).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingStataCode`)
3. Commit your Changes (`git commit -m 'Add some AmazingStataCode'`)
4. Push to the Branch (`git push origin feature/AmazingStataCode`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
