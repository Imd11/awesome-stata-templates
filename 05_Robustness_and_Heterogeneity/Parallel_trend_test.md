# Parallel trend test

```r
use "D:\000Alternate Desktop\Sino-German Intelligent Manufacturing\Data\panel\panel_malm",clear
xtset stock_id year
winsor2 h size grow pay age cash lev roe indratio dual numb wg, replace cuts(1 99)
global z "size   age  lev   dual numb wg"

replace first_treat=0 if first_treat==.
gen period = year - first_treat

gen pre_9 = treat*(period==-9)
gen pre_8 = treat*(period==-8)
gen pre_7 = treat*(period==-7)
gen pre_6 = treat*(period==-6)
gen pre_5 = treat*(period==-5)
gen pre_4 = treat*(period==-4)
gen pre_3 = treat*(period==-3)
gen pre_2 = treat*(period==-2)
gen pre_1 = treat*(period==-1)
gen current = treat*(period==0)
gen post_1=treat*(period==1)
gen post_2=treat*(period==2)
gen post_3=treat*(period==3)
gen post_4=treat*(period==4)
gen post_5=treat*(period==5)

drop pre_1

xtreg h pre_* current post_* $z i.year, fe 

coefplot, baselevels omitted // /
keep(pre_* current post_*) // /
coeflabels(pre_9="-9" pre_8="-8" pre_7="-7" pre_6="-6" pre_5="-5" pre_4="-4" pre_3="-3" // /
pre_2="-2"   current="0"  post_1="1"  post_2="2"  post_3="3"  post_4="4" post_5="5") // /
vertical  // /transpose graphics
addplot(line @b @at, lcolor(gs1) ) // /Add connections between points
title("Figure 1 Parallel Trend Test",size(4.5) position(6) margin(medium))//  /
ytitle(`"{fontface "宋体": estimated coefficient}"', margin(small))//  /
xtitle(`"{fontface "宋体": relative to the time of policy implementation (year)}"')//  /
yline(0) levels( 95 )  // /
ylabel(-0.05 "-0.05" 0.0 "0" 0.05 "0.05") // /
msymbol(O) msize(small) mcolor(gs1) // /plot style
ciopts(recast(rcap) lpattern(dash) lcolor(gs2)) scheme(s1mono) // CI is the upper and lower seals on the dotted line
```

