# Related analysis export

```diff
*Relevance table
use panel, clear
estpost correlate y x $z ,matrix
esttab using table - correlation and significance results.rtf, unstack not noobs compress nogap replace star(* 0.1 ** 0.05 *** 0.01) b(%9.4f)

*Correlation visualization
graph matrix y x $z,scheme(s1mono) msize(tiny) mcolor(black)
```

regression analysis


```diff

reg Willingness to participate Age Education level Cognition of low-carbon life Low-carbon behavior Promotion difficulties Related measures
est sto reg
esttab reg using table-regression.rtf, r2 obslast nogaps star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace
```

