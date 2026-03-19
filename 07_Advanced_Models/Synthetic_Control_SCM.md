# Synthetic control SCM

```diff
*Synthetic control method
*synth h Lev ROA ROE NetProfit Liquid Quick Cashflow INV Growth AssetGrowth // /
h(2014) h(2015) h(2016) h(2017) h(2018), trunit(35) trperiod(2019) xperiod(2014(1)2018) // /
keep(synth)

use synth.dta, clear
gen effect= _Y_treated - _Y_synthetic+0.05
label variable _time "year"
label variable effect "gap in per-capita cigarette sales (in packs)"
line effect _time, xline(2019,lp(dash)) yline(0,lp(dash)) graphregion(fcolor(white)) scheme(s2manual) xlabel(2014(1)2022) xtitle("Year")
```

# explain

The basic syntax format of synth is as follows:

```diff
synth depvar predictorvars(x1 x2 x3) , trunit(#) trperiod(#)   // /
   [ counit(numlist) xperiod(numlist) mspeperiod()  // /
   resultsperiod() nested allopt unitnames(varname) // /
   figure keep(file) customV(numlist) optsettings ]
```

The specific explanation is as follows:

- " y " is the outcome variable (outcome variable)
- " x1 x2 x3 " is the predictor variable (predictors).
- The required option " trunit(#) " is used to specify the processing area (trunit means treated unit).
- The required option " trperiod(#) " is used to specify the period when policy intervention starts (trperiod means treated period).
- The option " counit(numlist) " is used to specify potential control regions (i.e., donor pool, where counit represents control units), which defaults to all regions in the data set except the treatment region.
- The option "
- The option " mspeperiod() " is used to specify the period that minimizes the mean square prediction error (MSPE), which defaults to all periods before the start of policy intervention.
- The option "figure" indicates that the result variables of the processing area and synthetic control will be drawn into a time trend graph, and the option "resultsperiod()" is used to specify the time range of this graph (the default is the entire sample period).
- The option "nested" means to use a nested numerical method to find the optimal synthetic control (this option is recommended), which is more time-consuming than the default method, but may be more accurate. When using the selection item "nested", if you add the selection item " allopt " (that is, " nested allopt "), it will take more time than using "nested" alone, but the accuracy may be higher.
- The option "keep(filename)" saves the estimation results (e.g., weights of synthetic controls, outcome variables) as another Stata data set (filename.dta) for subsequent calculations.
#California Tobacco Control Case

Background: In November 1988, California passed the largest anti-tobacco legislation in the United States in contemporary times, and it came into effect in January 1989. The law raised California's cigarette excise tax by 25 cents per pack, earmarked the proceeds for tobacco control education and media campaigns, and triggered a series of local clean indoor-air ordinances, such as bans on smoking in restaurants and enclosed workplaces. Abadie et al. (2010) used the synthetic control method to study the effect of California's 1988 Tobacco Control Law No. 99 (Proposition 99) based on interstate panel data from 1970 to 2000 in the United States.

```diff
. sysuse smoking (open data set)
. xtset state year (set to panel data)
. synth cigsale retprice lnincome age15to24 beer  // /
    cigsale(1975) cigsale(1980) cigsale(1988),    // /
    trunit(3)trperiod(1989) xperiod(1980(1)1988)  // /
    figure nested keep(smoking_synth)
```

The specific explanation is as follows:

- cigsale(1975) cigsale(1980) cigsale(1988) represent the values ​​of per capita cigarette consumption in 1975, 1980 and 1988 respectively.
- The required option "trunit(3)" indicates that the third state (i.e. California) is the treatment group (experimental subject).
- The required option "trperiod(1989)" indicates that the tobacco control law was implemented in 1989 (the policy implementation time point).
- The option "xperiod(1980(1)1988)" means to average the predictor variables during 1980-1988, where "1980(1)1988" means starting in 1980, with intervals of 1 year, and ending in 1988; its effect is equivalent to "1980 1981 1982 1983 1984 1985 1986 1987 1988", and the former is obviously more concise.
- Select the option "keep(smoking_synth)" to save the estimation results as the Stata data set smoking_synth.dta (automatically stored in the current working path).


