#Group samples

1. How to press the number of records to a certain variable in stata. For example, income is grouped from low to high.

for example:

There is a variable y: the values ​​of y are: 1 2 3 4 5 6

I want to divide it into 2 groups, high and low, 50% each, and generate a new variable. If y belongs to high, group=1, if it is low, group=0

I tried xtile, ptile, _ptile, and I was confused. I thought it should be one of these three commands.

My intention is to group the variables by income, as there is a command that does that easily. All I can do now is the stupid way (divided into ten groups from high to low):

```stata
sort y
gen group=1
forvalue i=2/10 {
replace group=`i' if _n>_N/10*(`i'-1)
}
```



