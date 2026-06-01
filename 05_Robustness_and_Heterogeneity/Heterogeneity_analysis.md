#Heterogeneity analysis

```stata

**Heterogeneity
use panel3, clear

xtreg h Int1 $z i.year if Province=="Beijing City"|Province=="Tianjin Province"|Province=="Hebei Province"|Province=="Shanghai City"|Province=="Jiangsu Province"|Province=="Zhejiang Province"|Provinc e=="Fujian Province"|Province=="Shandong Province"|Province=="Guangdong Province"|Province=="Hainan Province"|Province=="Liaoning Province"|Province=="Jilin Province"|Province=="Heilongjiang" , fer
est sto heterogeneous east 1

xtreg h Int1 $z i.year if Province=="Shanxi Province"|Province=="Anhui Province"|Province=="Jiangxi Province"|Province=="Henan Province"|Province=="Hubei Province"|Province=="Hunan Province", fe r
est sto heterogeneity 1

xtreg h Int1 $z i.year if Province=="Inner Mongolia Autonomous Region"|Province=="Guangxi Province"|Province=="Chongqing City"|Province=="Sichuan Province"|Province=="Guizhou Province"|Province=="Yunnan Province"| Province=="Shaanxi Province"|Province=="Gansu Province"|Province=="Qinghai Province"|Province=="Ningxia Province"|Province=="Xinjiang Uygur Autonomous Region"|Province=="Tibet" , fer
est sto heterogeneous west 1



esttab heterogeneity* using table-heterogeneity analysis-region.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace

```

### Cluster analysis in heterogeneity analysis

```stata
*Heterogeneity in economic development levels
use test malm, clear
collapse (mean) GDP per capita yuan, by (city)//  Average value of each region in panel data
cluster wardslinkage GDP per capita yuan
cluster gen type1=group(3)
cluster dendrogram, cutnumber(13) ylabel(0(5000000000)20000000000, angle(horizontal))  yline(1190000000) scheme(s1mono)
keep id type1

save cluster analysis results, replace
use test malm, clear
merge m:1 id using cluster analysis results,nogen
xtreg y1 x $z  i.year if type1==3, fe r
est sto yreg_j1
xtreg y1 x $z  i.year if type1==2, fe r
est sto yreg_j2
xtreg y1 x $z  i.year if type1==1, fe r
est sto yreg_j3
esttab yreg_j* using Table - Economic development level heterogeneity.rtf, r2 obslast nogaps drop (*year*) star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) se(%6.4f) r2(%6.4f) compress replace
```

