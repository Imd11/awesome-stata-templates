# placebo test

```diff
**Individual-time dimension
use panel, clear
cap erase "simulations.dta"
permute did beta = _b[did] se = _se[did] df = e(df_r), // /
 reps(500) rseed(123) saving("simulations.dta"): // /
  reghdfe y did $z , absorb(fid10 year) vce(robust)

*Regression coefficient chart
use "simulations.dta", clear
gen t_value = beta / se
gen p_value = 2 * ttail(df, abs(beta/se))

dpplot beta, msymbol(smcircle_hollow)  // /
 xline(0.0275, lc(black*0.5) lp(dash)) // /
 xline(0, lc(black) lp(solid)) // /
 xlabel(-0.01(0.01)0.01) // /
title("Figure 7 Placebo Test",size(4.5) position(6) margin(medium))//  /
xtitle(`"{fontface "宋体":false estimation coefficient}"', size(*1)) xlabel(, format(%3.2f) labsize(small))//  /
ytitle(`"{fontface "宋体": probability density}"', size(*1)) ylabel(, nogrid format(%3.0f) labsize(small))//  /
    note("") caption("") graphregion(fcolor(white)) 
```



```r
*-Placebo test 1
*-Randomly generate treatment groups-individual dimension
use panel,clear
cap erase "simulations.dta"
permute treatment beta = _b[c.treatment#c.post] se = _se[c.treatment#c.post] df = e(df_r), // /
 reps(500) rseed(123) saving("simulations1.dta",replace): // /
  reghdfe lnfirst c.treatment#c.post nou_rate lnasset lnmj , absorb(county year) vce(robust)

 // regression coefficient
use "simulations1.dta", clear
gen t_value = beta / se
gen p_value = 2 * ttail(df, abs(beta/se))

dpplot beta, // /
xline(0.1216, lc(black*0.5) lp(dash)) msymbol(smcircle_hollow) // /
xline(0, lc(black*0.5) lp(solid)) // /
xtitle(`"{fontface "宋体":false estimation coefficient}"', size(*2.5)) xlabel(-0.14(0.04)0.14, format(%4.2f) labcolor(black) labsize(huge)) xscale(range(-0.14 0.14))//  /
ytitle(`"{fontface "宋体": probability density}"', size(*2.5)) ylabel(, nogrid format(%4.2f) labsize(huge))//  /
note("") caption("") graphregion(fcolor(white)) // /
title(`"{fontface "宋体":(a) Randomly generated processing group}"', size(*2) position(6) margin(small) )//  /
saving(placebo test-randomly generate treatment group.gph, replace)


*-Placebo test 2-when the policy change occurs-time dimension
use panel,clear
cap erase "simulations2.dta"
permute post beta = _b[c.treatment#c.post] se = _se[c.treatment#c.post] df = e(df_r), // /
 reps(500) rseed(123) saving("simulations2.dta",replace): // /
  reghdfe lnfirst c.treatment#c.post, absorb(county year) vce(robust)

 // regression coefficient
use "simulations2.dta", clear
gen t_value = beta / se
gen p_value = 2 * ttail(df, abs(beta/se))

dpplot beta, // /
xline(0.1216, lc(black*0.5) lp(dash)) msymbol(smcircle_hollow) // /
xline(0, lc(black*0.5) lp(solid)) // /
xtitle(`"{fontface "宋体":false estimation coefficient}"', size(*2.5)) xlabel(-0.14(0.04)0.14, format(%4.2f) labcolor(black) labsize(huge)) xscale(range(-0.14 0.14))//  /
ytitle(`"{fontface "宋体": probability density}"', size(*2.5)) ylabel(, nogrid format(%4.2f) labsize(huge))//  /
note("") caption("") graphregion(fcolor(white)) // /
title(`"{fontface "宋体":(b) Randomly set the time when the policy occurs}"', size(*2) position(6) margin(small) )//  /
saving(placebo test-randomly set the time when the policy occurs.gph, replace)

graph combine placebo test-randomly generate treatment groups.gph placebo test-randomly set the time when the policy occurs.gph,//  /
              row(1) // /
			  xsize(15) ysize(5)    // /
			  scheme(s1mono) // /
			  graphregion(ifcolor(white))
graph export placebo test.png, replace
```







