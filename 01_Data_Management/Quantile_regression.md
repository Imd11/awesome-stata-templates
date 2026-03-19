# Quantile regression

```javascript
sqreg TFP_LP Supply chain finance level SOE Lev Growth Board Top1 FirmAge, q(0.25,0.50,0.75)
est sto regf
esttab regf using "table-quantile regression.rtf", r2 obslast nogaps star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace
```





