# Roadmap

This roadmap describes the near-term maintenance direction for `awesome-stata-templates`.

## Project Scope

`awesome-stata-templates` is a practical template library for Stata users working on empirical economics, finance, and social science research.

The project focuses on reusable snippets and workflow examples for:

- data import, cleaning, reshaping, and panel setup
- descriptive statistics and correlation analysis
- baseline regression and fixed effects models
- endogeneity checks and instrumental variable workflows
- robustness, heterogeneity, and mechanism analysis
- advanced empirical methods such as PSM-DID and synthetic control
- export utilities for regression tables and research outputs

## Non-Goals

This repository is not intended to be:

- a compiled Stata package
- a replacement for econometrics textbooks or method-specific documentation
- a source of dataset-specific empirical conclusions
- a guarantee that a template is valid for every research design

Users are expected to adapt each template to their own data structure, identification strategy, and reporting requirements.

## Near-Term Priorities

### v0.1.0: Maintainable Template Library

- Add contribution guidelines.
- Add issue and pull request templates.
- Add a template index and method taxonomy.
- Improve README navigation.
- Add a changelog and release checklist.

### v0.2.0: Lightweight Quality Checks

- Add Markdown and repository structure checks.
- Standardize code block language tags where safe.
- Document common placeholder variable conventions.
- Add basic validation for template headings and required sections.

### v0.3.0: Research Workflow Coverage

- Improve reusable examples for common empirical workflows.
- Add more guidance for panel fixed effects, DID, event studies, and table export.
- Add notes about required community-contributed Stata commands where templates depend on them.

## Maintenance Principles

- Prefer small, reviewable pull requests.
- Avoid broad rewrites of existing templates unless the method-specific behavior is preserved.
- Keep examples copy-paste friendly, but make assumptions explicit.
- Use documentation and validation to reduce contributor and maintainer workload.
