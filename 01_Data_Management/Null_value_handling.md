#Null value handling



R&D funds R&D personnel R&D headcount
366328100.69		
22703291.90		
3935626.54		
7386392.27		
9170000		
20154830690.00		
18377791.33		
12887735.07



If you cannot clean it directly, you can consider creating a new numerical variable to store the numerical information of "R&D personnel". For example:

```stata
gen R&D number = real (R&D personnel)
The real() function attempts to convert character variables to numeric types.
```

Finally try again

```stata
replace R&D headcount=0 if missing(R&D headcount)
```

