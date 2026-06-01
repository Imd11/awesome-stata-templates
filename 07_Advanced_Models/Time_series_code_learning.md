# Time series code learning

```stata
* Period-by-period growth calculation: ai-a(i-1) (ie: an − a(n-1))
gen  zg_GDP   =GDP[_n]   - GDP[_n-1]	
gen  zg_EYTP  =EYTP[_n]  - EYTP[_n-1]	
gen  zg_BR    =BR[_n]    - BR[_n-1]	
gen  zg_PCGDP =PCGDP[_n] - PCGDP[_n-1]	
gen  zg_NHC   =NHC[_n]   - NHC[_n-1]	
gen  zg_NHB   =NHB[_n]   - NHB[_n-1]	
gen  zg_ABPHF =ABPHF[_n] - ABPHF[_n-1]	

* Calculation of cumulative growth: ai − a0 (ie: an − a1)
gen  lg_GDP   =GDP[_n]   - GDP[1]	
gen  lg_EYTP  =EYTP[_n]  - EYTP[1]	
gen  lg_BR    =BR[_n]    - BR[1]	
gen  lg_PCGDP =PCGDP[_n] - PCGDP[1]	
gen  lg_NHC   =NHC[_n]   - NHC[1]	
gen  lg_NHB   =NHB[_n]   - NHB[1]	
gen  lg_ABPHF =ABPHF[_n] - ABPHF[1]	

* The sum of the period-by-period growth amounts during the period is equal to the cumulative growth amount during the period: ai − a0 (ie: an − a1)
gen  lj_GDP  =sum(zg_GDP) 
gen  lj_EYTP =sum(zg_EYTP) 
gen  lj_BR   =sum(zg_BR) 
gen  lj_PCGDP=sum(zg_PCGDP) 
gen  lj_NHC  =sum(zg_NHC)
gen  lj_NHB  =sum(zg_NHB)	
gen  lj_ABPHF=sum(zg_ABPHF) 	

*The difference between two adjacent cumulative growth amounts is equal to the period-by-period growth amount of the corresponding period: ai-a(i-1) (ie: an − a(n-1))
gen  zq_GDP   =lg_GDP[_n]   - lg_GDP[_n-1]	
gen  zq_EYTP  =lg_EYTP[_n]  - lg_EYTP[_n-1]	
gen  zq_BR    =lg_BR[_n]    - lg_BR[_n-1]	
gen  zq_PCGDP =lg_PCGDP[_n] - lg_PCGDP[_n-1]	
gen  zq_NHC   =lg_NHC[_n]   - lg_NHC[_n-1]	
gen  zq_NHB   =lg_NHB[_n]   - lg_NHB[_n-1]	
gen  zq_ABPHF =lg_ABPHF[_n] - lg_ABPHF[_n-1]	

*Example 2.2: Average growth
*Example 2.2.1: Horizontal method
gen  spf_GDP   =sum(zg_GDP)	 /[_n] 			
gen  spf_EYTP  =sum(zg_EYTP) /[_n] 			
gen  spf_BR    =sum(zg_BR)	 /[_n]  			
gen  spf_PCGDP =sum(zg_PCGDP)/[_n] 			
gen  spf_NHC   =sum(zg_NHC)	 /[_n]  			
gen  spf_NHB   =sum(zg_NHB)	 /[_n]  			
gen  spf_ABPHF =sum(zg_ABPHF)/[_n] 	 		 

*Example 2.2.2: Cumulative method
gen  ljf_GDP    =2*sum(lg_GDP)	/ ([_n]*[_n+1])	
gen  ljf_EYTP   =2*sum(lg_EYTP)	/ ([_n]*[_n+1])	
gen  ljf_BR 	=2*sum(lg_BR)	/ ([_n]*[_n+1])	
gen  ljf_PCGDP  =2*sum(lg_PCGDP)/ ([_n]*[_n+1])	
gen  ljf_NHC 	=2*sum(lg_NHC)	/ ([_n]*[_n+1])	
gen  ljf_NHB 	=2*sum(lg_NHB)	/ ([_n]*[_n+1])	
gen  ljf_ABPHF 	=2*sum(lg_ABPHF)/ ([_n]*[_n+1])	

*2.3 Development speed
use "D:\1work\Changli\003-Student Training\4-Undergraduate Training\20230613-Undergraduate Courses\20230813-Undergraduate Courses-Statistics\20230824-Lecture Notes Design\Chapter 8 Time Series Analysis\Chapter 8 Time Series Analysis (Data Analysis)\Example 2.1: Growth Index.dta",clear
drop EYTP BR PCGDP NHC NHB ABPHF 
*2.3.1 Calculation of chain development speed:
gen  hb_GDP   =GDP[_n]   / GDP[_n-1]	
gen  hb_EYTP  =EYTP[_n]  / EYTP[_n-1]	
gen  hb_BR    =BR[_n]    / BR[_n-1]		
gen  hb_PCGDP =PCGDP[_n] / PCGDP[_n-1]	
gen  hb_NHC   =NHC[_n]   / NHC[_n-1]	
gen  hb_NHB   =NHB[_n]   / NHB[_n-1]	
gen  hb_ABPHF =ABPHF[_n] / ABPHF[_n-1]	

*2.3.2 Calculation of fixed base development speed:
gen  db_GDP   =GDP[_n]   / GDP[1]	
gen  db_EYTP  =EYTP[_n]  / EYTP[1]	
gen  db_BR    =BR[_n]    / BR[1]	
gen  db_PCGDP =PCGDP[_n] / PCGDP[1]	
gen  db_NHC   =NHC[_n]   / NHC[1]	
gen  db_NHB   =NHB[_n]   / NHB[1]	
gen  db_ABPHF =ABPHF[_n] / ABPHF[1]	

*2.3.3 The continuous product of each chain development speed in a certain period of time is equal to the fixed base development speed in that period:
*lhb_GDP calculation
gen lhb_GDP = 1
quietly forval i = 2/`=_N' {
    replace lhb_GDP = lhb_GDP[_n-1] * hb_GDP if _n == `i'
}
*
gen lhb_EYTP = 1
quietly forval i = 2/`=_N' {
    replace lhb_EYTP = lhb_EYTP[_n-1] * hb_EYTP if _n == `i'
}
*
gen lhb_BR = 1
quietly forval i = 2/`=_N' {
    replace lhb_BR = lhb_BR[_n-1] * hb_BR if _n == `i'
}
*
gen lhb_PCGDP = 1
quietly forval i = 2/`=_N' {
    replace lhb_PCGDP = lhb_PCGDP[_n-1] * hb_PCGDP if _n == `i'
}
*
gen lhb_NHC = 1
quietly forval i = 2/`=_N' {
    replace lhb_NHC = lhb_NHC[_n-1] * hb_NHC if _n == `i'
}
*
gen lhb_NHB = 1
quietly forval i = 2/`=_N' {
    replace lhb_NHB = lhb_NHB[_n-1] * hb_NHB if _n == `i'
}
*
gen lhb_ABPHF = 1
quietly forval i = 2/`=_N' {
    replace lhb_ABPHF = lhb_ABPHF[_n-1] * hb_ABPHF if _n == `i'
}

*2.3.4 The difference between two adjacent cumulative growth amounts is equal to the period-by-period growth amount of the corresponding period:
gen  ldb_GDP   =db_GDP[_n]   / db_GDP[_n-1]	
gen  ldb_EYTP  =EYTP[_n]  	 / EYTP[_n-1]		
gen  ldb_BR    =db_BR[_n]    / db_BR[_n-1]	
gen  ldb_PCGDP =db_PCGDP[_n] / db_PCGDP[_n-1]		
gen  ldb_NHC   =db_NHC[_n]   / db_NHC[_n-1]		
gen  ldb_NHB   =db_NHB[_n]   / db_NHB[_n-1]		
gen  ldb_ABPHF =db_ABPHF[_n] / db_ABPHF[_n-1]		

*2.3.5 Speed ​​ratio = development speed of phenomenon a/development speed of phenomenon b:
use "D:\1work\Changli\003-Student Training\4-Undergraduate Training\20230613-Undergraduate Courses\20230813-Undergraduate Courses-Statistics\20230824-Lecture Notes Design\Chapter 8 Time Series Analysis\Chapter 8 Time Series Analysis (Data Analysis)\Example 2.1: Growth Index.dta",clear
drop BR PCGDP NHC NHB ABPHF 
gen  GDP_EYTP1=GDP /EYTP 		 // Direct ratio of GDP to EYTP
gen  db_GDP   =GDP[_n]   / GDP[1]	
gen  db_EYTP  =EYTP[_n]  / EYTP[1]	
gen  GDP_EYTP=db_GDP /db_EYTP 	 // The ratio of GDP development speed to EYTP development speed
* Let’s compare the difference between “the ratio of GDP development speed and EYTP development speed” and “the direct ratio of GDP and EYTP”.


*2.4Growth rate
*2.4.1 Ratio growth rate
gen  hbzs_GDP   =GDP[_n]   / GDP[_n-1]		- 1
gen  hbzs_EYTP  =EYTP[_n]  / EYTP[_n-1]		- 1
gen  hbzs_BR    =BR[_n]    / BR[_n-1]		- 1
gen  hbzs_PCGDP =PCGDP[_n] / PCGDP[_n-1]	- 1
gen  hbzs_NHC   =NHC[_n]   / NHC[_n-1]		- 1
gen  hbzs_NHB   =NHB[_n]   / NHB[_n-1]		- 1
gen  hbzs_ABPHF =ABPHF[_n] / ABPHF[_n-1]	- 1

*2.4.2 Fixed base growth rate
gen  dbzs_GDP   =GDP[_n]   / GDP[1]		- 1
gen  dbzs_EYTP  =EYTP[_n]  / EYTP[1]	- 1
gen  dbzs_BR    =BR[_n]    / BR[1]		- 1
gen  dbzs_PCGDP =PCGDP[_n] / PCGDP[1]	- 1
gen  dbzs_NHC   =NHC[_n]   / NHC[1]		- 1
gen  dbzs_NHB   =NHB[_n]   / NHB[1]		- 1
gen  dbzs_ABPHF =ABPHF[_n] / ABPHF[1]	- 1

*2.4.3 Growth rate
*Horizontal method calculates average development speed
gen  pjfzsd_GDP   = db_GDP^(1/_n)	
gen  pjfzsd_EYTP  = db_EYTP^(1/_n)	
gen  pjfzsd_BR    = db_BR^(1/_n)		
gen  pjfzsd_PCGDP = db_PCGDP^(1/_n)	
gen  pjfzsd_NHC   = db_NHC^(1/_n)		
gen  pjfzsd_NHB   = db_NHB^(1/_n)
gen  pjfzsd_ABPHF = db_ABPHF^(1/_n)	


*Horizontal method calculates average growth rate
gen  pjzzsd_GDP   = db_GDP^(1/_n)	 - 1
gen  pjzzsd_EYTP  = db_EYTP^(1/_n)	 - 1
gen  pjzzsd_BR    = db_BR^(1/_n)	 - 1	
gen  pjzzsd_PCGDP = db_PCGDP^(1/_n)	 - 1
gen  pjzzsd_NHC   = db_NHC^(1/_n)	 - 1	
gen  pjzzsd_NHB   = db_NHB^(1/_n) 	 - 1
gen  pjzzsd_ABPHF = db_ABPHF^(1/_n)	 - 1



```

