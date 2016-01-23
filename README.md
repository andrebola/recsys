# recsys

with rels.json in /tmp:


```import src.system
a = src.system.System('makam_artists', 'alg', 10, 1, 'artist', 'artist')
s = src.system.System('sys1', 'sys', 10, 1, 'artist', 'artist', [a])
s.recommend(['4b593731-0f81-4e90-ad7a-ffd6be17c5cd'])```
