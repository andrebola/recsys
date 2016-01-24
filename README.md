# recsys

with rels.json in /tmp:

```
import src.system
a = src.system.System('makam_artists', 'alg', 10, 1, 'artist', 'artist')
s = src.system.System('sys1', 'sys', 10, 1, 'artist', 'artist', [a])
s.recommend(['4b593731-0f81-4e90-ad7a-ffd6be17c5cd'])
```


For quering though the web 

```
  {"name": "sys1", "s_type": "sys", "limit": 10, "weight": 1, "input_type": "artist", "output_type": "artist", "next_s": null, "components": [{"name": "makam_artists", "s_type": "alg", "limit": 10, "weight": 1, "input_type": "artist", "output_type": "artist", "next_s": null, "components": []}]}  
```

```
4b593731-0f81-4e90-ad7a-ffd6be17c5cd
```
