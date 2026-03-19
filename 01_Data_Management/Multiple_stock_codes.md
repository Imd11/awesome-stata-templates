# Multiple tickers/columns

1. Stata, if there are two stock codes (separated by commas), the stock codes are divided into columns, a new row is generated, and the values ​​of other variables are copied.

Stock code Latest disclosure date Start time
000681.S	20081222	265
600103.S	20071122	256
600103.S	20071122	36
600137.S	20061228	965
600615.S	20050204	65
900922.S,600689.S	20041116	45
200505.S,000505.S	20030927	88
600881.S	20030314	84
600108.S	20020630	461
000503.S	20020630	646



```javascript
use ss, clear
gen multiple_stocks = strpos(stock code, ",") > 0
split stock code, parse(",") generate(stock code)

* Split stock symbol variable
gen long id = _n

* Generate new rows
expand 2 if multiple_stocks == 1

bys id: gen long id1 = _n

egen a=max(id1)
forval i =1/2{
replace stock code = stock code `i' if id1==`i'
}

* Clean up generated variables
drop multiple_stocks - a
```



# 2. stata, extract year:

Statistics deadline
2008-12-31
2009-12-31
2010-12-31
2011-12-31

```javascript
gen year = substr(statistical deadline, 1, 4)
destring year, replace
```

# 3. stata, extraction date:

This is a date in %td format, the code is as follows

```diff
gen year = year (announcement date)//  Year of extraction
gen month=month(announcement date)//  Extract month
```

