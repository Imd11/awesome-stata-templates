# Breakpoint regression and instrumental variable regression

```javascript
**Breakpoint regression
use panel, clear

rdplot h year, c(2017)
```



```javascript
use panel, clear                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
gen g=Number of post and telecommunications offices at the end of the year*l. Number of Internet users per 100 people
ivregress 2sls y Level of economic development Level of financial development1 Degree of opening up Fiscal investment Fiscal decentralization Level of human capital Level of industrialization Level of marketization Employment structure (x=g), first
est sto nreg tool variable
estat endogenous
estat firststage
```

