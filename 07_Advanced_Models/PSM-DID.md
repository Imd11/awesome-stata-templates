# PSM-DID

```r
***************Core matching
use "D:\000Alternate Desktop\Sino-German Intelligent Manufacturing\Data\panel\panel_ate",clear
xtset stock_id year
winsor2 Y size grow pay age cash lev roe indratio dual numb wg, replace cuts(1 99)
global z "size grow pay age cash lev roe indratio dual numb wg"

psmatch2 treat $z, out(Y) logit ate kernel
pstest $z, both graph

drop if _support==0|_support==.

areg Y did  i.year, absorb(stock_id) r
est store psmkreg1
areg Y did $z i.year  , absorb(stock_id) r
est store psmKreg2
*************Nearest neighbor matching
use "D:\000Alternate Desktop\Sino-German Intelligent Manufacturing\Data\panel\panel_ate",clear
xtset stock_id year
winsor2 Y size grow pay age cash lev roe indratio dual numb wg, replace cuts(1 99)
global z "size grow pay age cash lev roe indratio dual numb wg"

psmatch2 W $z, out(Y) logit ate neighbor(1)
pstest $z

drop if _support==0|_support==.

areg Y did  i.year, absorb(stock_id) r
est store psmnreg1
areg Y did $z i.year  , absorb(stock_id) r
est store psmnreg2

***************Radius matching
use "D:\000Alternate Desktop\Sino-German Intelligent Manufacturing\Data\panel\panel_ate",clear
xtset stock_id year
winsor2 Y size grow pay age cash lev roe indratio dual numb wg, replace cuts(1 99)
global z "size grow pay age cash lev roe indratio dual numb wg"

psmatch2 W $z, out(Y) logit ate neighbor(2) caliper(0.05) ties 
pstest $z

drop if _support==0|_support==.

areg Y did  i.year, absorb(stock_id) r
est store psmrreg1
areg Y did $z i.year  , absorb(stock_id) r
est store psmrreg2


esttab psm* using "D:\000substitute desktop\Sino-German Intelligent Manufacturing\data\panel\table-PSM-DID.rtf", r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace
```





# Match year by year

```diff
*****************************psm-did********************
***Variable description
*$x: Global temporary element representing covariates
*Y: interpreted variable
*treated: dummy variable for treatment group


***Step one: Carry out PSM year by year and save the PSM results of each year, and finally obtain the matched data set for a total of 10 years from 1998 to 2007.
forvalue i = 1998/2007{
      preserve
          capture {
              keep if year == `i'
              set seed 0000
              gen  norvar_2 = rnormal()
              sort norvar_2

              psmatch2 treated $x , outcome(Y) logit neighbor(2)  // /
                                        ties common ate caliper(0.05)

              save `i'.dta, replace
              }
      restore
      }  

clear all


***Step 2: Merge all data vertically, merge the matched data of each year into one data set vertically, and generate the panel data we need for regression
use 1998, clear
forvalue k =1999/2007 {
      capture {
          append using `k'.dta
          }
      }
save data, replace


***Step 3: Kernel density plot of propensity score values
sum _pscore if treated == 1, detail  // Assume that the calculated mean propensity score for the treatment group is 0.5698

*Before matching

sum _pscore if treated == 0, detail

twoway(kdensity _pscore if treated == 1, lpattern(solid)                     // /
              lcolor(black)                                                  // /
              lwidth(thin)                                                   // /
              scheme(qleanmono)                                              // /
ytitle("{stSans:core}""{stSans:crypt}""{stSans:degree}",//  /
                     size(medlarge) orientation(h))                          // /
xtitle("{stSans: propensity score value before matching}",//  /
                     size(medlarge))                                         // /
              xline(0.5698   , lpattern(solid) lcolor(black))                // /
              xline(`r(mean)', lpattern(dash)  lcolor(black))                // /
              saving(kensity_yby_before, replace))                           // /
      (kdensity _pscore if treated == 0, lpattern(dash)),                    // /
      xlabel(     , labsize(medlarge) format(%02.1f))                        // /
      ylabel(0(1)3, labsize(medlarge))                                       // /
legend(label(1 "{stSans:processing group}")//  /
label(2 "{stSans:Control group}")//  /
             size(medlarge) position(1) symxsize(10))

graph export "kensity_yby_before.emf", replace

discard

*After matching

sum _pscore if treated == 0 & _weight != ., detail

twoway(kdensity _pscore if treated == 1, lpattern(solid)                     // /
              lcolor(black)                                                  // /
              lwidth(thin)                                                   // /
              scheme(qleanmono)                                              // /
ytitle("{stSans:core}""{stSans:crypt}""{stSans:degree}",//  /
                     size(medlarge) orientation(h))                          // /
xtitle("{stSans: propensity score value after matching}",//  /
                     size(medlarge))                                         // /
              xline(0.5698   , lpattern(solid) lcolor(black))                // /
              xline(`r(mean)', lpattern(dash)  lcolor(black))                // /
              saving(kensity_yby_after, replace))                            // /
      (kdensity _pscore if treated == 0 & _weight != ., lpattern(dash)),     // /
      xlabel(     , labsize(medlarge) format(%02.1f))                        // /
      ylabel(0(1)3, labsize(medlarge))                                       // /
legend(label(1 "{stSans:processing group}")//  /
label(2 "{stSans:Control group}")//  /
             size(medlarge) position(1) symxsize(10))



***Step 4: Year-by-year balance inspection
*- before matching

forvalue i = 1998/2007 {
          capture {
              qui: logit treated $xlist i.ind3 if year == `i', vce(cluster prov)
              est store ybyb`i'
              }
          }

local ybyblist ybyb1998 ybyb1999 ybyb2000 ybyb2001 ybyb2002                  // /
               ybyb2003 ybyb2004 ybyb2005 ybyb2006 ybyb2007

reg2docx `ybyblist' using Year-by-year balance test results_before matching.docx, b(%6.4f) t(%6.4f)//  /
         scalars(N r2_p(%6.4f)) noconstant replace                           // /
         indicate("Industry = *.ind3")                                       // /
         mtitles("1998b" "1999b" "2000b" "2001b" "2002b"                     // /
                 "2003b" "2004b" "2005b" "2006b" "2007b")                    // /
title("Year-by-year balance test_before matching")

*- after matching

forvalue i = 1998/2007 {
          capture {
              qui: logit treated $xlist i.ind3                               // /
                       if year == `i' & _weight != ., vce(cluster prov)
              est store ybya`i'
              }
          }

local ybyalist ybya1998 ybya1999 ybya2000 ybya2001 ybya2002                  // /
               ybya2003 ybya2004 ybya2005 ybya2006 ybya2007

reg2docx `ybyalist' using Year-by-year balance test results_after matching.docx, b(%6.4f) t(%6.4f)//  /
         scalars(N r2_p(%6.4f)) noconstant replace                           // /
         indicate("Industry = *.ind3")                                       // /
         mtitles("1998a" "1999a" "2000a" "2001a" "2002a"                     // /
                 "2003a" "2004a" "2005a" "2006a" "2007a")                    // /
title("Year-by-year balance test_after matching")



```

