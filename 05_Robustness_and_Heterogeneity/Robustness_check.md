# Robustness check

## 1. Control other forms of fixed effects

Considering that the development level of enterprise intelligent manufacturing may be affected by the characteristic factors of the city where the enterprise is located, and some city characteristic factors may be dynamically adjusted over time, in model (2), in model (2), the city and year interaction fixed effects, year fixed effects and individual fixed effects are simultaneously controlled. The results show that the coefficient of the did variable is 0.0293 with a significance level of 1%, which further confirms the robustness of the benchmark results.

```stata
use "panel_malm",clear
xtset stock_id year
reghdfe h did size   age  lev   dual numb wg  , absorb(i.city#i.year city id year) 
est store reg interaction fixed
```





```stata

*Endogeneity test
*Core explanatory variables are lagged by one period
xtreg h l.Int1 $z i.year, fe 
est sto robustness1

*Control variables are lagged by one period
xtreg h Int1 l.Size l.Lev l.ROE l.Growth l.Board l.Indep l.Dual l.TMTPay2 l.FirmAge l.Cashflow i.year, fe 
est sto robustness 2

*Interaction fixed effects
egen proid=group(Province)
reghdfe h Int1 $z , absorb(i.proid#i.year) 
est sto robustness 3

esttab robustness* using table-robustness test.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace


```

