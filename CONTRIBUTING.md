# Contributing

Thank you for helping improve `awesome-stata-templates`.

This repository is a practical template library for Stata users working on empirical economics, finance, and social science research. Contributions should make templates easier to find, understand, adapt, or maintain.

## Good Contributions

Good pull requests usually do one of the following:

- add a reusable Stata template for a common empirical workflow;
- improve the explanation around an existing template;
- fix unclear placeholder variables or assumptions;
- improve repository navigation or documentation;
- add lightweight validation that helps maintainers review future templates.

Avoid mixing unrelated changes in one pull request. A documentation update, a template rewrite, and a CI change should usually be separate PRs.

## Template Format

When adding a new template, use this structure where possible:

````markdown
# Method or Workflow Name

## Purpose

Explain what the template does in one or two sentences.

## When to Use

Describe the research scenario where this template is appropriate.

## Required Variables

- `y`: outcome variable
- `x`: main explanatory variable
- `controls`: control variables
- `id`: panel or unit identifier
- `time`: time variable

## Stata Template

```stata
* Replace placeholders with project-specific variables.
xtset id time
xtreg y x controls i.time, fe vce(cluster id)
```

## Notes

Document assumptions, required packages, and common adjustments.
````

If an existing template is intentionally short, it does not need to be expanded aggressively. Prefer minimal edits that make the snippet clearer without changing its meaning.

## Placeholder Variable Conventions

Use consistent placeholder names when possible:

| Placeholder | Meaning |
| --- | --- |
| `y` | outcome or dependent variable |
| `x` | main explanatory variable |
| `controls` | control variable list |
| `id` | unit, firm, individual, region, or panel identifier |
| `time` | year, month, quarter, or other time variable |
| `treat` | treatment group indicator |
| `post` | post-treatment period indicator |
| `did` | treatment-by-post interaction |
| `cluster_id` | clustering unit for standard errors |

Existing templates may use other variable names when they come from a specific example. When changing them, make sure the code remains understandable and methodologically equivalent.

## Stata Code Blocks

Use fenced code blocks with the `stata` language tag:

````markdown
```stata
reg y x controls, vce(robust)
```
````

Do not use `javascript`, `r`, or `diff` for Stata code. Those tags make GitHub highlighting misleading.

## Required Package Notes

If a template depends on a community-contributed Stata command, mention it in the notes. Examples include:

- `winsor2`
- `reghdfe`
- `psmatch2`
- `esttab`
- `outreg2`
- `reg2docx`
- `logout`

Where appropriate, include a short installation hint:

```stata
ssc install reghdfe
```

## Pull Request Checklist

Before opening a PR, check:

- [ ] The PR has one clear purpose.
- [ ] New Stata code blocks use the `stata` language tag.
- [ ] Placeholder variables are documented or easy to replace.
- [ ] Required community commands are noted.
- [ ] The template does not include private file paths or sensitive data.
- [ ] Existing template behavior is preserved unless the PR explains the change.
- [ ] Documentation links are valid.

## Review Expectations

Maintainers review for:

- clarity of the research use case;
- copy-paste friendliness;
- consistency with existing folder categories;
- explicit assumptions and required packages;
- minimal unrelated formatting churn.

Small, focused PRs are easier to review and merge.
