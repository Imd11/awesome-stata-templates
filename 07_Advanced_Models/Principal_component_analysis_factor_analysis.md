# Principal component analysis factor analysis







```stata
use data, clear
*Test of sphericity
factortest X1-X12

// pca X1-X12

factor X1-X12,pcf mineigen(1)
rotate

predict f1 f2 
*************************
. predict f1 f2 
(option regression assumed; regression scoring)

Scoring coefficients (method = regression)

    ----------------------------------
        Variable |  Factor1   Factor2 
    -------------+--------------------
              X1 |  0.29765  -0.06135 
              X2 |  0.02044  -0.39582 
              X3 |  0.10851   0.07587 
              X4 | -0.01150   0.33735 
              X5 |  0.03716  -0.18688 
              X6 |  0.00000   0.00000 
              X7 |  0.12436  -0.01290 
              X8 |  0.11936   0.11522 
              X9 |  0.10070  -0.00435 
             X10 |  0.12248  -0.02487 
             X11 |  0.12325  -0.07968 
             X12 |  0.06171   0.34729 
    ----------------------------------
************************






screeplot, yline(1) // Gravel chart

gen f=0.7820*f1+0.2180*f2
```

