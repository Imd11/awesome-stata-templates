# Multicollinearity test

This study conducted a strict test on multicollinearity among explanatory variables, and the results are presented in Table 4.3. Usually, the determination of multicollinearity relies on the variance inflation factor (VIF). According to the generally accepted VIF test standard, when the VIF value of a variable is in the interval of 1<VIF<10, the multicollinearity between variables is within the acceptable range. Observing Table 4.3, MeanVIF (mean VIF), as a key indicator to measure the overall degree of multicollinearity, has a value of 2023, which is in the reasonable interval of 1<VIF<10, and all variables meet this standard. This shows that based on the comprehensive evaluation of the data in Table 4.3 based on the VIF test criterion, there is no multicollinearity problem among the relevant explanatory variables in this study. This result laid a solid data foundation for subsequent model construction and analysis.



Table 4.3 Multicollinearity test





```javascript
reg y $z 
estat vif
```

