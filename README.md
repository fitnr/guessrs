# guessrs

Tries to match source coordinates against state plane, UTM, and several national projections.

Example:
```
$ guessrs 2180123.68 1167481.35 2344933.16 1259185.56 -90.583534 39.872503 -89.994405 40.125292
6457	NAD83(2011) / Illinois West (ftUS)	-0.00190	0.00059	-0.00063	0.00092
```

The elements of the command are: 
* A bounding box in an unknown projection: `2180123.68 1167481.35 2344933.16 1259185.56`
* The known bounding box (in geographic coordinates) of the mapped region: `-90.5835 39.8725 -89.9944 40.1252`

The result is tab-delimited, with the following fields: EPSG code, projection name, the difference between the source coordinates and the target in this projection.

