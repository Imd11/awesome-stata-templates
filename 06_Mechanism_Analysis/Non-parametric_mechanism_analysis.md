# Non-parametric mechanism analysis

```javascript
bootstrap r(ind_eff) r(dir_eff) , reps(1000) seed(101): sgmediation density0 , mv( tauL2 ) iv( did ) cv(lngdp second  sciexpe   scier   sto)
estat bootstrap, percentile bc   // Confidence intervals expressed as percentiles and bias corrected

```

