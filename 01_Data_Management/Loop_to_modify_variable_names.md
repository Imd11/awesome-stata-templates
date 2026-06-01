# Loop to modify variable names

Delete y in variable names in batches:

```stata
foreach var of varlist y population density (person/square kilometer) city (region) - y total industrial output value above designated size (current price, 10,000 yuan) city (region) {
  local newvar : subinstr local var "y" ""
  rename `var' `newvar'
}
```





