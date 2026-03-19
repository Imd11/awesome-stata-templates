# Descriptive Statistics

Export of common descriptive analysis results:

```javascript
*Descriptive statistics
use data, clear
logout, save(table-descriptive statistics) word replace: tabstat density0 lngdp, by(treat) statistics(mean sd min max count)
```



```javascript
**Descriptive statistics
use data, clear
keep TFP_LP Supply Chain Finance Level SOE Lev Growth Board Top1 FirmAge
outreg2 using table-descriptive statistics results.doc, replace sum(log) title(Descriptive statistics)
```



