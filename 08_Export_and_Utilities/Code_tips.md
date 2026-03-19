# Code tips

In stata, #delimit;

In Stata, #delimit; is a command used to change the end character of a command. By default, Stata's command terminator is a newline character, that is, each line is treated as an independent command. However, if you want a command to span multiple lines, you can use the #delimit ; ​​command to change the terminator to a semicolon. This way, Stata will treat the semicolon as the end of the command rather than a newline character.

For example:

```plain text
#delimit ;
gen y = x1 + x2
+ x3 + x4;

```

In this example, gen y = x1 + x2 + x3 + x4; is one command, even though it spans two lines. This command ends on a semicolon, not a newline.



