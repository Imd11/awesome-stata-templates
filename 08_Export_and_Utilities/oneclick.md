# oneclick

```stata
oneclick y Size Lev ROA ROE  NetProfit , fix(x i.year) p(0.01) m(xtreg) o(fe r)
```





```stata
collapse (mean) industrial structure 2 x, by (year)//  Panel data average for each year

tw (line x year, lpattern(solid)) (line industrial structure 2 year, lpattern(dash))
```





```stata
use data1, clear

oneclick y Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of opening to the outside world Market size 1 Level of marketization Employment structure Ten thousand employees, fix(lnx i.year) p(0.05) m(xtreg) o(fe r)

use oneclick_subset, clear
save benchmark is significant, replace

*************Agent 1===
use data1, clear
oneclick Industrial structure 1 Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of openness to the outside world Market size 1 Level of marketization Employment structure Ten thousand people employed, fix(lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m11 significant
save m11 significant, replace

use data1, clear
oneclick y Economic agglomeration level Economic development level Foreign investment level Urbanization level Infrastructure Opening up to the outside world Market size 1 Marketization level Employment structure 10,000 employees, fix(industrial structure 1 lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m12 inverse significant
save m12 inverse significant, replace
*************Agency 2
use data1, clear
oneclick Overall upgrade of industrial structure Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of opening to the outside world Market size 1 Level of marketization Employment structure Ten thousand employees, fix(lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m21 significant
save m21 significant, replace

use data1, clear
oneclick y Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of opening to the outside world Market size 1 Level of marketization Employment structure Ten thousand employees, fix (overall upgrade of industrial structure lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m22 inverse significant
save m22 inverse significance, replace

*************Agency 3===
use data1, clear
oneclick Advanced industrial structure Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of opening to the outside world Market size 1 Level of marketization Employment structure Ten thousand people employed, fix(lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m31 significant
save m31 significant, replace

use data1, clear
oneclick y Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of openness to the outside world Market size 1 Level of marketization Employment structure Ten thousand employees, fix (advanced industrial structure lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m32 inverse significant
save m32 inverse significant, replace
*************Agency 4
use data1, clear
oneclick Rationalization of industrial structure Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of opening to the outside world Market size 1 Level of marketization Employment structure Ten thousand employees, fix(lnx i.year) p(0.1) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m41 significant
save m41 significant, replace

use data1, clear
oneclick y Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Infrastructure Degree of opening to the outside world Market size 1 Level of marketization Employment structure Ten thousand employees, fix (rationalization of industrial structure lnx i.year) p(0.1) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m42 inverse significant
save m42 inverse significant, replace

*************Agency 5
use data1, clear
gen Number of utility models obtained in the year 10,000 = Number of utility models obtained in the year/10000
oneclick Number of utility models obtained in the year 10,000 Level of economic agglomeration Level of economic development Level of foreign investment Level of urbanization Level of infrastructure Opening up to the outside world Market size 1 Level of marketization Employment structure 10,000 employees , fix(lnx i.year) p(0.1) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m51 significant
save m51 significant, replace

use data1, clear
oneclick y Economic agglomeration level Economic development level Foreign investment level Urbanization level Infrastructure Opening degree Market size 1 Marketization level Employment structure 10,000 employees, fix(market openness lnx i.year) p(0.05) m(xtreg) o(fe r)
use oneclick_subset, clear
keep subset direction
rename direction m52 inverse significant
save m52 inverse significant, replace
****************************************
use benchmark is significant, clear
merge 1:1 subset using m11 significant
keep if _merge==3
drop _merge

merge 1:1 subset using m12 inverse significant
keep if _merge==3
drop _merge

merge 1:1 subset using m21 significant
keep if _merge==3
drop _merge

merge 1:1 subset using m22 inverse significant
keep if _merge==3
drop _merge


merge 1:1 subset using m41 significant
keep if _merge==3
drop _merge

merge 1:1 subset using m42 inverse significant
keep if _merge==3
drop _merge
save significant retention, replace


















```

