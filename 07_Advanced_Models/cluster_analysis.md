# Cluster analysis

```stata
cluster wardslinkage GDP per capita yuan
cluster gen type1=group(3)
cluster dendrogram, cutnumber(13) ylabel(0(5000000000)20000000000, angle(horizontal))  yline(1190000000) scheme(s1mono)
```

