#The variable takes the 30th percentile





```diff
sum h, detail
egen h30 = pctile(h), p(10)
```

