#Interaction fixed effects

```stata
*Interaction fixed effects
use data, clear
reghdfe density0 did lngdp second sciexpe scier sto , absorb(i.provincial administrative code#i.year provincial administrative code municipal administrative code year)
est sto rb_jh
```



