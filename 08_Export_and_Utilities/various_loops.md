# Various loops

```stata
*Retain variables "new_*" whose minimum value is less than 0

foreach var of varlist new* {
    qui summarize `var'
    local min = r(min)
    if `min' > 0 {
        drop `var'
    }
}
```



```stata
foreach city of varlist Beijing-Urumqi {
gen treat_`city' = self-created district policy year if city == "`city'"
}  // Equivalent to first_year

foreach var of varlist treat_Beijing-treat_Urumqi {
	egen first_`var' = max(`var')
	}

foreach city of varlist Beijing-Urumqi {
gen activate_`city'=`city'*(year>=first_treat_`city')
}	




*count
forval i = 50(50)1000 {
    local j = `i' - 50
    gen count_`i' = 0
foreach var of varlist activate_Beijing-activate_Urumqi {
        replace count_`i' = count_`i' + (`j' < `var' & `var' <= `i')
    }
}
```





```stata
forval i=2000/2021 {
    gen lnD2_`i'=lnD2*(year==`i')
}
```

In stata, let the number of Internet users in the country be
National telecommunications business revenue in 10,000 yuan
Tens of thousands of fixed-line users nationwide at the end of the year
Tens of thousands of mobile phone users nationwide at the end of the year
Multiply by the province_number of post and telecommunications offices at the end of the year
Province_Number of telephone sets at the end of the year
Province_The total volume of postal and telecommunications business at the end of the year is 10,000 yuan
Province_number of post offices per million people per year
Province_Number of landline telephones per 100 people per year
Province_Number of telephones per 10,000 people
For each item, generate a new variable z* and write a loop (double loop nesting)

```stata
local vars "Number of Internet users nationwide. National telecommunications business revenue in 10,000 yuan. Tens of thousands of fixed-line users nationwide. Tens of thousands of mobile phone users nationwide."
local factors "Province_number of post and telecommunications offices at the end of the year Province_number of telephone sets at the end of the year Province_total postal and telecommunications business at the end of the year 10,000 Yuan Province_number of post offices per million people per year Province_number of fixed telephones per 100 people per year Province_number of telephone sets per 10,000 people"

foreach v of local vars {
    foreach f of local factors {
        gen z_`v'_`f' = `v' * `f'
    }
}
```



Stata deletes variables containing missing values ​​and specifies all variables for looping:

```stata
foreach var of var _all {
    qui sum `var', meanonly
    if r(N) > 0  drop `var'
}
```





```stata
Loop statement in stata
forvalues i =8(-1)1{
 gen pre_`i'=(treatment==1&period==-`i') 
}
gen current = (treatment==0&period==0)
forvalues j =1(1)4{
 gen post_`j'=(treatment==1&period==`j') 
} 
```

