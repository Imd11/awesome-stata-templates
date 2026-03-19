# Baseline regression

```javascript
use panel, clear  
xtreg y x  i.year ,fe r
est sto xtreg1
xtreg y x $z  i.year ,fe r
est sto xtreg2
esttab xtreg* using table-benchmark regression.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace
```



