# Missing value imputation

By variable, use its own linear trend interpolation (suitable for fewer missing values):

```javascript
foreach var of varlist Completed investment in residential development (10,000 yuan) in the city (region) - Number of industrial enterprises above designated size in the city (region) {
	bys city: ipolate `var' year, gen(new_`var') epolate
}
```

According to the variable, use its own linear trend to perform missing value interpolation:

```javascript
*3. Fill in missing values
egen city=group(city)
xtset city year
foreach var of varlist Residential development investment completion amount (10,000 yuan) city (region) - highway freight volume (10,000 tons) city (region) {
    replace `var' = . if `var' == .
    qui xtreg `var' year , fe
    predict `var'_imp if `var' == .                              // The newly generated "var_imp" is the predicted value of the missing value of "var".
	replace `var'=`var'_imp if `var' == .                        // Interpolate the predicted value into the original variable "var".
}
drop *_imp
```

By city, by variable, interpolation is performed using the linear relationship between the variable and the regional GDP (there is no missing value in this variable) (applicable to many missing values):

```javascript
foreach var of varlist Completed investment in residential development (10,000 yuan) in the city (region) - Number of industrial enterprises above designated size in the city (region) {
    replace `var' = . if `var' == .	
gen `var'_imputed data=.
	forval i =1/16 {
		 reg `var' gdp if city==`i'
		 predict `var'_imp if (`var' == .)&(city==`i')         // The newly generated "var_imp" is the predicted value of the missing value of "var".
replace `var'_imputation data=`var'_imp if city==`i'//  Keep imputed data
replace `var'=`var'_interpolated data if (`var' == .)&(city==`i')//  Interpolate the predicted value into the original variable "var".
		 drop `var'_imp
	}                                         
}
```



