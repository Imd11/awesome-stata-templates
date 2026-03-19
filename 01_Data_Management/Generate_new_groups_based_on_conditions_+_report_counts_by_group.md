# Generate new groups based on conditions + report counts by group

1. Use stata for data processing and report the H02 situation of various industries. H02 is divided into these groups according to numbers: 0, 1-4, 5-7, 8-19, 20-30, 31-50, 51 and above. Report the counting status of each industry and each H02

```javascript
gen group =.
replace group = 1 if H02 == 0
replace group = 2 if inrange(H02, 1, 4)
replace group = 3 if inrange(H02, 5, 7)
replace group = 4 if inrange(H02, 8, 19)
replace group = 5 if inrange(H02, 20, 30)
replace group = 6 if inrange(H02, 31, 50)
replace group = 7 if H02 > 50
tabulate industry_final group // Perform tabulate statistics on industries and groups
```

Running results:

```javascript


Judgment based on information from multiple parties |
Disrupted industries (complete | group
lost) | 1 2 3 4 | Total
----------------------+--------------------------------------------+----------
Transportation, warehousing and postal services.. | 21 25 23 27 | 120
Information transmission, software and information.. | 66 65 59 43 | 259
Agriculture, forestry, animal husbandry and fishery | 188 89 41 37 | 401
Manufacturing | 140 74 86 164 | 775
Real Estate | 28 30 14 38 | 153
House construction, civil engineering.. | 45 50 58 57 | 267
Education, health, social work.. | 65 95 43 53 | 315
Water conservancy, environment and public facilities.. | 7 2 2 4 | 18
Electricity, heat, gas and... | 4 4 1 4 | 19
Scientific research and technical services | 55 49 39 65 | 263
Leasing and business services | 154 164 101 160 | 708
Mining | 1 0 0 0 | 6
Financial Industry | 0 3 3 3 | 15
----------------------+--------------------------------------------+----------
                Total |       774        650        470        655 |     3,319 


Judgment based on information from multiple parties |
Disrupted industries (complete | group
lost) | 5 6 7 | Total
----------------------+---------------------------------+----------
Transportation, warehousing and postal services.. | 15 5 4 | 120
Information transmission, software and information.. | 6 9 11 | 259
Agriculture, forestry, animal husbandry and fishery | 23 12 11 | 401
Manufacturing | 128 77 106 | 775
Real Estate | 14 14 15 | 153
House construction, civil engineering.. | 37 7 13 | 267
Education, health, social work.. | 24 16 19 | 315
Water conservancy, environment and public facilities.. | 1 1 1 | 18
Electricity, heat, gas and... | 2 0 4 | 19
Scientific research and technical services | 29 11 15 | 263
Leasing and business services | 61 20 48 | 708
Mining | 0 2 3 | 6
Financial Industry | 4 0 2 | 15
----------------------+---------------------------------+----------
                Total |       344        174        252 |     3,319 

```

