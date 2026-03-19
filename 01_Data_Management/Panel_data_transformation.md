#Panel data transformation

Invert the data. For example, in the panel data, the time range is 2011-2011, replace the 2011 point data with 2022, replace the 2012 data with 2021, and so on.

```diff
use panel1, clear
keep code year h
gen new_year = 2022 - (year - 2011)
drop year
rename new_year year
sort code year
save h, replace // match again
```



