#Technological innovation efficiency-malmq2

```stata
**********************************Technological Innovation Efficiency******************************************
use panel_h, clear
sort stock_id year
xtset stock_id year
malmq2 rd rd_inco caprd rder rder_pr = patent mbi lev , dmu(stock_id) saving(malm) ort(o) rd // Requires: Stata version 16


```

```stata

use malm,clear
gen year=substr(Pdwise,-4,.)
destring year,replace
drop Pdwise Row
save malm_match, replace
*match
use panel_h, clear
merge 1:1 stock_id year using malm_match
drop if _merge==2
save panel_malm, replace
```



