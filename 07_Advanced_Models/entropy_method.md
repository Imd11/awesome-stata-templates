# Entropy method

```stata
**********************Define the entropy value program************************
capture program drop shangzhi
program shangzhi
args var statue rn // var: The variable to be processed, status=1 indicates a positive indicator, status=-1 indicates a negative indicator, rn: the product of r year and n observations
quietly{
*step1 normalize `var'_sd
sum `var' 
scalar min=r(min)
scalar max=r(max)

g `var'_sd=(`var'-min)/(max-min)
if `statue'==-1{
noisily dis as error "negative indicator"
replace `var'_sd=1-`var'_sd
}

*step2 Calculate the proportion `var'_sdw
g  `var'_sds= `var'_sd+0.00000001 // Note: Add offset 0.00000001, which can be modified by yourself
egen `var'_sds_sum=sum(`var'_sds) // Calculate the sum of `var'_sds
g  `var'_sdw=`var'_sds / `var'_sds_sum // Calculate the proportion of `var'_sds

*step3 Calculate entropy value `var'_s
g `var'_sij=-1*`var'_sdw*ln(`var'_sdw)/ln(`rn') // `var'_sij
egen `var'_s=sum(`var'_sij) // Entropy value `var'_s

*step4 Calculate information utility `var'_g
g `var'_g=1-`var'_s

*step5 Clear redundant variables: only keep `var'_sd, `var'_g
drop `var'_sds `var'_sdw `var'_sds_sum `var'_sij `var'_s 
}
end
***********************************
*****************Main program*************

*【1】Find `var'_g
/*Call the shangzhi program and enter three parameters in sequence.
The variable var to be processed, the positive indicator or the negative indicator (1 or -1), the value of r*n (this article: 14*30=420, 14 years, 30 provinces and cities)
Note: Negative indicators will prompt text, but positive indicators will not*/

*Note, the following code can be modified as needed

*Negative indicator
// shangzhi v1 -1 420
// shangzhi v3 -1 420
// shangzhi v5 -1 420
*Positive indicator
shangzhi cipin1 1 6699
shangzhi Intangible Assets Intelligent Manufacturing 1 6699
shangzhi fixed assets intelligent manufacturing 1 6699


*[2] Find the weight wi
g sum_g=cipin1_g+intangible assets intelligent manufacturing_g+fixed assets intelligent manufacturing_g//  _g is the information utility value

gen w_cipin1=cipin1_g/sum_g
gen w_intangible assets intelligent manufacturing=intangible assets intelligent manufacturing_g/sum_g
gen w_fixed assets intelligent manufacturing=fixed assets intelligent manufacturing_g/sum_g


drop sum_g 
list w* in 1 // display weight

*【3】Find the final score hij
g h=cipin1_sd*w_cipin1+intangible assets intelligent manufacturing_sd*w_intangible assets intelligent manufacturing+fixed assets intelligent manufacturing_sd*w_fixed assets intelligent manufacturing
drop *_g *_sd
save "D:\000My Office Area\Master's Graduation\Thesis\Data-Original\panel\panel_h",replace
```





multivariable

```stata
*****************Main program*************

*【1】Find `var'_g
/*Call the shangzhi program and enter three parameters in sequence.
The variable var to be processed, the positive indicator or the negative indicator (1 or -1), the value of r*n (this article: 14*30=420, 14 years, 30 provinces and cities)
Note: Negative indicators will prompt text, but positive indicators will not*/

*Note, the following code can be modified as needed

*Negative indicator
foreach v of varlist Income Poverty Line Relative Income Engel's Coefficient Health Care Expenditures Physical Function Depression Life Satisfaction Elevator Use Bathing Toilet Broadband Internet Durable Goods {
	shangzhi `v' -1 34150
}


*[2] Find the weight wi
egen sum_g=rowtotal(*_g) // _g is the information utility value

foreach v of varlist Income Poverty Line Relative Income Engel's Coefficient Health Care Expenditures Physical Function Depression Life Satisfaction Elevator Use Bathing Toilet Broadband Internet Durable Goods {
	gen w_`v'=`v'_g/sum_g
}




drop sum_g 
list w* in 1 // display weight

*【3】Find the final score hij
gen h =0
foreach v of varlist Income Poverty Line Relative Income Engel's Coefficient Health Care Expenditures Physical Function Depression Life Satisfaction Elevator Use Bathing Toilet Broadband Internet Durable Goods {
	replace h=`v'_sd*w_`v'+h
}


drop *_g *_sd
```

