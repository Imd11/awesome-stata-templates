#99Difficult and complicated diseases

## 1、ereturn clear

"ereturn clear" is a Stata command used to clear the results of the most recent command. It is commonly used to clear return results between commands in Stata programs. For example:

```plain text
regress y x1 x2
ereturn clear
logit y x1 x2
```

In this example, we first run a regression command and then use "ereturn clear" to clear the return results of the command. We then ran a logistic regression command without being affected by the results returned by the previous command.

Note that if you type "ereturn clear" in the Stata command window, it will clear the results of the most recent command.

