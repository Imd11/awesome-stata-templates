# Clean-Other

Replace variables less than 0 variables with the previous period

```javascript
foreach var of varlist new* {       // Keep variables less than 0
    qui summarize `var'
    local min = r(min)
    if `min' > 0 {
        drop `var'
    }
}

sort city year
foreach var of varlist new* {
	bys city: replace `var' = l.`var' if `var' < 0
}
```

If the Postal and Telecommunications Bureau is missing at the end of 2017 and subsequent years, it will be replaced by the data lagged 5 periods of this variable by randomly adding or subtracting 2;

```javascript
// If the post office is missing at the end of the year, replace it with the lag of 5 periods of the variable, randomly adding or subtracting 2 by 2.
replace year-end post and telecommunications office = l5. year-end post and telecommunications office + 4 * round(runiform()) - 2 if year-end post and telecommunications office ==.
```

Stata removes variables containing missing values

```javascript
foreach var of var _all {
    qui sum `var', meanonly
    if r(N) > 0  drop `var'
}
```

Variable name case:

```javascript
// Get all variable names
unab vars: _all
// Change all variable names to uppercase
foreach var in `vars' {
    local new_name = upper("`var'")
    rename `var' `new_name'
}
rename TIMESTAMP timestamp
```



Replace Beijing City with Beijing

```javascript
replace province = subinstr(province, "autonomous region", "", .)
replace province = subinstr(province, "city", "", .)
replace province = subinstr(province, "province", "", .)
replace province = subinstr(province, "Hui", "", .)
replace province = subinstr(province, "Zhuang", "", .)
replace province = subinstr(province , "Uyghur", "", .)
```



Check the length of householdID and if it is only 9 digits add 0 at the end

householdID
0101041010
0101041010
0101041010
0101041010
0101041010
0101041010
010104101
010104101

```diff
* Check the length of householdID, if it is only 9 digits, add 0 at the end

* 1. Generate a new variable to store the modified householdID
gen new_householdID = householdID

* 2. Use the len() function to check the length of each householdID
* If the length is 9, add 0 at the end
replace new_householdID = householdID + "0" if length(householdID) == 9

* Show results
list householdID new_householdID, clean
```

Extract the last digit of a variable:

ID
01010410102
01010410101
010104101001
010104101002

```diff
* Extract the last digit of each ID

* 1. Generate a new variable to store the last digit of each ID
gen last_digit = substr(ID, length(ID), 1)

* Show results
list ID last_digit, clean
```

## Column merge

```diff
gen dynamic relative indicator 1 = string(dynamic relative indicator, "%9.2f") + "%"
```

1. First use the string() function to convert the original numeric variable dynamic_relative_index into a character type, where "%9.2f" specifies the conversion format, which is similar to the format meaning in the format command introduced before. Make sure that the value is converted in an appropriate format (here, two decimal places are retained, etc.). You can adjust this format specifier according to actual needs.
1. Then through the string concatenation operation (using the + symbol), add the "%" symbol after the converted character data, and store the result in the newly generated variable new_variable.
