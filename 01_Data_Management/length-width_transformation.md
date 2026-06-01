# Length and width transformation

```markdown
reshape long y, i(region indicator) j(year)
```

```markdown
reshape wide y, i(region year) j(index) string
```

```stata
foreach var of varlist y regional GDP - y secondary industry added value {
  local newvar : subinstr local var "y" ""
  rename `var' `newvar'
}                                                                // Modify variable name
```



## Case 2

```stata
reshape long task completion time screen dizziness space disorientation, i (subject number) j (platform)
```

