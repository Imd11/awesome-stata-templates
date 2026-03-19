#digital economy/digital inclusive finance

Organize area names

```javascript
use digital inclusive finance, clear
keep Province Region Year Digital Financial Inclusion Index
replace region="Beijing City" if province=="Beijing City"
replace region="Shanghai City" if province=="Shanghai City"
replace region="Tianjin City" if province=="Tianjin City"
replace region="Chongqing City" if province=="Chongqing City"
collapse (mean) digital financial inclusion index, by (region year)
```

