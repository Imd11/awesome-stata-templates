# Panel data extends for one year

```stata
expand 2 if year==2020,gen(d)
replace year=2021 if d==1
```

