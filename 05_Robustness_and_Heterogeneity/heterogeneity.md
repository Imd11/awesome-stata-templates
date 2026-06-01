# heterogeneity

```stata
gen region=1 if provinces=="Beijing City"|provinces=="Tianjin City"|provinces=="Hebei Province"|provinces=="Shandong Province"|provinces=="Jiangsu Province"|provinces=="Shanghai City"|provinces=="Zhejiang Province"|provinces=="Fujian Province"|provinces=="Guangdong Province"|provinces=="Hainan Province"|provinces=="Liaoning Province"
replace region=2 if provinces=="Shanxi Province"|provinces=="Anhui Province"|provinces=="Jiangxi Province"|provinces=="Henan Province"|provinces=="Hubei Province"|provinces=="Hunan Province"
replace region=3 if region==.
```



