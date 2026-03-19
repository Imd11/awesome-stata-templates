#Import and export data

```javascript
import excel China Urban Statistics Panel Data 2000-2022.xlsx, sheet("Sheet1") firstrow clear
export excel using delete data anguogao-xin.xlsx, firstrow(variables) replace

import delimited balance sheet.csv, clear
```

