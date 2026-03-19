# City Statistical Yearbook Processing

### 1. Generate province code based on city code

data:

```javascript
tostring administrative division code, replace
gen province code = substr(administrative division code, 1, 2) + "0000"
```



