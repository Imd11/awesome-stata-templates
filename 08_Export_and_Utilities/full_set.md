#full set

**Child Page:** Company-Code

```javascript

***********************
use panel, clear
global z SOE Size Lev ROE Growth Board Dual

*baseline regression
xtreg y x i.year, fe r
est sto xtreg1
xtreg y x $z i.year, fe r
est sto xtreg2
esttab xtreg* using table-benchmark regression.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace




**Robustness check
*Replace the explained variable
use panel, clear
xtreg y x2 $z i.year, fe r
est sto wregt

*Interaction fixed effects
use panel, clear
egen proid=group(Province)
reghdfe y x $z , absorb(i.proid#i.year code) 
est sto wreg interaction fixed effects

*Quantile regression
sqreg y x $z , q(0.25,0.50,0.75)
est sto wreg quantile regression


esttab wreg* using table-robustness test.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace


**Endogeneity analysis

*The explained variable is prepended by one period
use panel, clear
sort id year
xtreg f.y x $z i.year, fe r
est sto nreg is interpreted variable prepended one period
*Control variables are lagged by one period
use panel, clear
xtreg y x l.SOE l.Size l.Lev l.ROE l.Growth l.Board l.Dual i.year, fe r
est sto nreg control variable is lagged by one period

esttab nreg* using table-endogeneity analysis.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace




**Heterogeneity analysis
*Regional heterogeneity
use panel, clear
xtreg y x $z i.year if East==1 , fe r
est sto regional heterogeneity east 1

xtreg y x $z  i.year if Mid==1, fe r
est sto regional heterogeneity 1

xtreg y x $z i.year if West==1 , fe r
est sto regional heterogeneity west 1
esttab regional heterogeneity* using table-regional heterogeneity.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace



*Heterogeneity of factor inputs
use panel, clear
xtreg y x $z i.year if labor intensive==1, fe r
est sto factor input heterogeneity labor-intensive

xtreg y x $z i.year if technology intensive==1, fe r
est sto factor input heterogeneity technology intensive

xtreg y x $z i.year if asset intensive==1, fe r
est sto factor input heterogeneous asset intensive

esttab factor input heterogeneity* using table-factor input heterogeneity.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace




*Mediating effect
use panel, clear
xtreg m x $z i.year , fe r
est sto m1

xtreg y x m $z i.year , fe r
est sto m2
esttab m1 m2 using table-mediation.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace



*Descriptive statistics
use panel, clear
logout, save(table-descriptive statistics) word replace: tabstat y x $z, by() statistics(mean sd min max count)


*Relevance table
use panel, clear
estpost correlate y x $z ,matrix
esttab using table - correlation and significance results.rtf, unstack not noobs compress nogap replace star(* 0.1 ** 0.05 *** 0.01) b(%9.4f)

*Correlation visualization
graph matrix y x $z ,scheme(s1mono) msize(tiny) mcolor(black)

```

```javascript
*Descriptive analysis
use panel, clear
logout, save (table - descriptive statistics) word replace: tabstat y

*Relevance
estpost correlate y
esttab using table - correlation and significance results.rtf, unstack not noobs compress nogap replace star(* 0.1 ** 0.05 *** 0.01) b(%9.4f)

*Correlation visualization
label variable x "digital economy"
Graph matrix y

**Baseline regression
use panel, clear
xtreg y x i.year, fe r
est sto xtreg1
xtreg y x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year, fe r
est sto xtreg2
esttab xtreg* using table-benchmark regression.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace

**Robustness check
*Replace the explained variable
use panel, clear
sort id year
malmq2 Total fixed asset investment of 10,000 yuan Tens of thousands of employees at the end of the year Industrial electricity consumption of 10,000 kilowatt-hours = Gross regional product of 10,000 yuan Industrial sulfur dioxide emissions in tons, dmu(id) saving(malm) ort(o)

use malm,clear
gen year=substr(Pdwise,-4,.)
destring year,replace
drop Pdwise Row
save malm_match, replace
*match
use panel, clear
merge 1:1 id year using malm_match
drop if _merge==2

xtreg TFPCH x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year, fe r
est sto wreg replaces the interpreted variable


*Interaction fixed effects
use panel, clear
egen proid=group(province)
reghdfe y x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure, absorb(i.proid#i.year)
est sto wreg interaction fixed effects

*Quantile regression
Sqreg y
est sto wreg quantile regression

esttab wreg* using table-robustness test.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace


**Endogeneity analysis
*Instrumental variables
use panel, clear
gen g=Number of post and telecommunications offices at the end of the year*l. Number of Internet users per 100 people
ivregress 2sls y Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure (x=g), first
est sto nreg tool variable
estat endogenous
estat firststage

*The explained variable is prepended by one period
use panel, clear
xtreg f.y x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year, fe r
est sto nreg is interpreted variable prepended one period
*Control variables are lagged by one period
use panel, clear
xtreg y x l. Level of economic development l. Degree of financial development 1 l. Degree of opening up to the outside world l. Fiscal investment intensity l. Fiscal decentralization l. Human capital level l. Industrialization level l. Marketization level l. Employment structure i.year, fe r
est sto nreg control variable is lagged by one period

esttab nreg* using table-endogeneity analysis.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace



**Heterogeneity analysis
*Regional heterogeneity
use panel, clear
xtreg y x Level of economic development Level of financial development1 Degree of opening to the outside world Fiscal investment intensity Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year if Province == "Beijing City" | Province == "Tianjin Province" | Province == "Hebei Province" | Province == "Shanghai City" | Province == "Jiangsu Province" | Province == "Zhejiang Province" | Province == "Fujian Province" | Province == "Shandong Province" | Province == "Guangdong Province" | Province == "Hainan Province" | Province == "Liaoning Province" | Province == "Jilin Province" | Province == "Heilongjiang", fe r
est sto regional heterogeneity east 1

Xtreg y
est sto regional heterogeneity 1

xtreg y x Level of economic development Level of financial development1 Degree of opening to the outside world Fiscal investment intensity Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year if Province == "Inner Mongolia Autonomous Region" | Province == "Guangxi Province" | Province == "Chongqing City" | Province == "Sichuan Province" | Province == "Guizhou Province" | Province == "Yunnan Province" | Province == "Shaanxi Province" | Province == "Gansu Province" | Province == "Qinghai Province" | Province == "Ningxia Province" | Province == "Xinjiang Uygur Autonomous Region" | Province == "Tibet", fe r
est sto regional heterogeneity west 1
esttab regional heterogeneity* using table-regional heterogeneity.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace


*Heterogeneity of urban nature
use panel, clear
xtreg y x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year if capitalcity==1, fe r
est sto heterogeneity of urban nature 1
xtreg y x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Human capital level Industrialization level Marketization level Employment structure i.year if capitalcity==0, fe r
est sto Urban heterogeneity 2
esttab urban nature heterogeneity* using table-urban nature heterogeneity.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace



**Mechanism analysis

*Intermediary-Green Technology Innovation
use panel, clear
xtreg m1 x Level of economic development Degree of financial development1 Degree of opening to the outside world Fiscal investment intensity Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year, fe r
est sto mreg12
xtreg y x m1 Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year, fe r
est sto mreg13

*Intermediary - the proportion of added value of the secondary industry in GDP
xtreg m2 x Level of economic development Level of financial development1 Degree of opening to the outside world Fiscal investment intensity Fiscal decentralization level Industrialization level Marketization level Internet penetration rate i.year, fe r
est sto mreg22
xtreg y x m2 Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization level Industrialization level Marketization level Internet penetration rate i.year, fe r
est sto mreg23

*Modulating effect
gen xz=x*z
xtreg y x xz Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure i.year, fe r
est sto zreg


esttab mreg* zreg using table-mechanism analysis.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace



**Space metering
use panel, clear
merge m:1 province using order
drop _merge
sort a year
collapse (mean) x y, by (province)//  Average value of each region in panel data
merge m:1 province using order
keep if _merge==3
drop _merge
sort a

spatwmat using w.dta,name(w) // Load matrix
spatgsa y,weights(w) moran // Compute Global Moran
// ssc install asdoc
asdoc spatgsa y,weights(w) moran // Output results to word

// Model selection
// /1) LM inspection
use w.dta,clear
spatwmat using w.dta,name(w) standardize 
spmat dta w C-AE, norm(row) replace // A-AE is the variable name
drop C-AE
set matsize 567
mat TMAT=I(21) // The number of years in parentheses
mat Wxt=TMAT#w // Merge the 27*27 section matrix with TMAT
svmat Wxt
save Wxt.dta,replace // Save the spatial panel weight matrix required for the M test
spatwmat using Wxt.dta,name(ww) standardize 

use panel, clear
collapse (mean) y
merge m:1 province using order
drop _merge
sort a year
xtset a year

*3. Fill in missing values
xtset a year
foreach var of varlist employment structure {
    replace `var' = . if `var' == .
    qui xtreg `var' year , fe
    predict `var'_imp if `var' == .                              // The newly generated "var_imp" is the predicted value of the missing value of "var".
	replace `var'=`var'_imp if `var' == .                        // Interpolate the predicted value into the original variable "var".
}
drop *_imp

reg y x 
spatdiag,w(ww) // LM test

// /2) HAUSMAN inspection
spatwmat using w.dta,name(w) standardize 
xsmle y x ,model(sdm) wmat(w) hausman nolog

// /3) LR inspection
spatwmat using w.dta,name(w) standardize 
xsmle y x ,fe model(sdm) wmat(w) type(time) nolog noeffects
est store sdm_a
xsmle y x ,fe model(sar) wmat(w) type(time) nolog noeffects
est store sar_a
xsmle y x ,fe model(sem) emat(w) type(time) nolog noeffects
est store sem_a
lrtest sdm_a sar_a // Compare sdm and sar models
lrtest sdm_a sem_a // Compare sdm and sem models


*return

xsmle y x ,fe model(sdm) wmat(w) type(both) nolog noeffects
est sto sdmreg1

xsmle y x Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure,fe model(sdm) wmat(w) type(both) nolog noeffects
est sto sdmreg2

esttab sdmreg1 sdmreg2 using table-space metric regression 1.rtf, r2 obslast nogaps star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace





```

