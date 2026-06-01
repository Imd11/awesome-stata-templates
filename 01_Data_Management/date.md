# date

2020-01-01 changes to date type, stata

```stata
generate stata_date = date(Date, "YMD")
format stata_date %td
gen year=year(date) // Year of extraction
```



