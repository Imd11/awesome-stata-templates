# Correlation analysis and export

```stata
***Correlation and result export
use data, clear
estpost correlate Liquidity Fin Lev Size ROA Top10 share,matrix
esttab using Table 4.3 Correlation and significance results.rtf, unstack not noobs compress nogap replace star(* 0.1 ** 0.05 *** 0.01) b(%9.4f)
```



