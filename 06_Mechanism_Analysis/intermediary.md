# intermediary

```stata
areg TFPCH did  $z  i.year , absorb(stock_id) r
est store zhongjie31
areg h TFPCH did  $z  i.year , absorb(stock_id) r
est store zhongjie32

esttab zhongjie* using "Table-Mediation Effect Test.rtf", r2 obslast nogaps drop(*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace

```



```stata
*sobel test
tab year, gen(year0)
tab stock_id, gen(stock_id0)
sgmediation h , iv( did ) mv( f1 ) cv($z year01-year012 stock_id01-stock_id0384)
sgmediation h , iv( did ) mv( f2 ) cv($z year01-year012 stock_id01-stock_id0384)
sgmediation h , iv( did ) mv( TFPCH ) cv($z year01-year012 stock_id01-stock_id0384)
```



```stata
bootstrap r(ind_eff) r(dir_eff), reps(500) : sgmediation h, mv(TECH) iv(did) cv($z)
```

