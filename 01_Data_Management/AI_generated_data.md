# AI generated data

Generate data:
The order of task completion time is Platform 4＜Platform 3＜Platform 2＜Platform 1; the order of screen dizziness score is Platform 4＜Platform 3＜Platform 1＜Platform 2; the order of space disorientation score is Platform 3＜Platform 4＜Platform 2＜Platform 1;
The stronger the spatial ability, the smaller the difference between groups in task completion time on different test platforms; the higher the familiarity with VR, the smaller the difference between groups in task completion time on different test platforms.

```javascript
*Clear data
clear

* Set random number seed to ensure repeatable results
set seed 12345

* Generate 21 subject IDs
set obs 30
gen subject serial number = _n

* Generate spatial ability and VR familiarity
gen spatial ability = round(runiform() * 10 + 10)
gen VR familiarity = round(runiform() * 5 + 5)

* Generate task completion time to ensure platform 4 < platform 3 < platform 2 < platform 1
gen task completion time 4 = round(runiform() * 10 + 20)
gen task completion time 3 = task completion time 4 + round(runiform() * 5 + 5)
gen task completion time 2 = task completion time 3 + round(runiform() * 5 + 5)
gen task completion time 1 = task completion time 2 + round(runiform() * 5 + 5)

* Generate screen dizziness score to ensure platform 4 < platform 3 < platform 1 < platform 2
gen screen dizziness 4 = round(runiform() * 5 + 5)
gen screen dizziness 3 = screen dizziness 4 + round(runiform() * 2 + 1)
gen screen dizziness 1 = screen dizziness 3 + round(runiform() * 2 + 1)
gen screen dizziness 2 = screen dizziness 1 + round(runiform() * 2 + 1)

* Generate a spatial disorientation score to ensure that platform 3 < platform 4 < platform 2 < platform 1
gen space lost 3 = round(runiform() * 5 + 5)
gen space lost 4 = space lost 3 + round(runiform() * 2 + 1)
gen space lost 2 = space lost 4 + round(runiform() * 2 + 1)
gen space lost 1 = space lost 2 + round(runiform() * 2 + 1)

* Calculate the standard deviation of the task completion time of each row
egen task completion time standard deviation = rowsd(task completion time 1 task completion time 2 task completion time 3 task completion time 4)

* Check the correlation coefficient between the standard deviation of task completion time and spatial ability
corr task completion time standard deviation spatial capability
scalar corr_sa = r(rho)

* Check the correlation coefficient between the standard deviation of task completion time and VR familiarity
corr task completion time standard deviation VR familiarity
scalar corr_vr = r(rho)

* If the correlation coefficient is positive, adjust the task completion time
while corr_sa > 0 | corr_vr > 0 {
    forvalues i = 1/21 {
scalar sa = spatial ability[`i']
scalar vr = VR familiarity[`i']
        scalar factor = (sa + vr) / 2

replace task completion time 4 = round(runiform() * 10 + 20) if _n == `i'
replace task completion time 3 = task completion time 4 + round(runiform() * 5 + 5) / factor if _n == `i'
replace task completion time 2 = task completion time 3 + round(runiform() * 5 + 5) / factor if _n == `i'
replace task completion time 1 = task completion time 2 + round(runiform() * 5 + 5) / factor if _n == `i'
    }

* Delete and recalculate the standard deviation of task completion time for each row
drop task completion time standard deviation
egen task completion time standard deviation = rowsd(task completion time 1 task completion time 2 task completion time 3 task completion time 4)

* Recheck the correlation coefficient between task completion time standard deviation and spatial ability
corr task completion time standard deviation spatial capability
    scalar corr_sa = r(rho)

* Re-examine the correlation coefficient between the standard deviation of task completion time and VR familiarity
corr task completion time standard deviation VR familiarity
    scalar corr_vr = r(rho)
}
```

