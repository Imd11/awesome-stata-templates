# Ranking

```stata
egen ranking = rank(-total score), unique
bysort total score: egen total score ranking=min(ranking)//  highest score ranking
sort total score
```

Small method:

```stata
gsort -var
gen ranking=_n
```





For multi-variable loops:

```stata
foreach v of varlist total score-h5 score{
egen `v'_prerank=rank(-`v'), unique
bysort `v' : egen `v' ranking=min(`v'_pre-ranking)//  highest score ranking
drop `v'_preranking
}
```



```stata
gsort -k l // The data is arranged in descending order by k and ascending order by l
```

