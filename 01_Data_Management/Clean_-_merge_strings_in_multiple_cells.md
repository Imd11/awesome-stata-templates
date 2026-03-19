# Clean-merge strings in multiple cells







The log is as follows:

. list

+------------------------+

| i   j          a     b |

|------------------------|

1. | 1   1      com 1   AAA |

2. | 1   2   firm abc   BBB |

3. | 2   1   firm def   AAA |

4. | 2   2      com 3   CCC |

5. | 2   3   firm 45c   AAA |

|------------------------|

6. | 2   4    com xyz   CCC |

7. | 3   1    com sdf   BBB |

8. | 3   2     com 1e   AAA |

9. | 3   3   firm ddx   CCC |

+------------------------+

.

. sort i j

. replace a=a+"/"+a[_n-1] if i==i[_n-1]

variable a was str8 now str31

(6 real changes made)

. replace b=b+"/"+b[_n-1] if i==i[_n-1]

variable b was str3 now str15

(6 real changes made)

. drop if i==i[_n+1]

(6 observations deleted)

. drop j

. list

+-------------------------------------------------------+

| i                                 a                 b |

|-------------------------------------------------------|

1. | 1                    firm abc/com 1           BBB/AAA |

2. | 2   com xyz/firm 45c/com 3/firm def   CCC/AAA/CCC/AAA |

3. | 3           firm ddx/com 1e/com sdf       CCC/AAA/BBB |

+-------------------------------------------------------+





## Case

Group according to event ID and subject party, and merge ipc classification numbers:

Code:

```diff
egen groupvar = group(event ID target party)
replace IPC classification number=IPC classification number+"/"+IPC classification number[_n-1] if groupvar==groupvar[_n-1]
drop if groupvar==groupvar[_n+1]
```

