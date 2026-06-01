# Calculate deflator

data:

Code:

```stata
g i=index_grp
replace i=index_grp*i[_n-1]/100 if year>1991
```



