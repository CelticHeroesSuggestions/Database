# Legacy Spawn Rates

* What: Increase the spawn chance of certain legacy bosses.
* Why: The content from those bosses is cool, but they are too rare.
* Notes: None.
* Changes:
```
# Lirs Reach: Bloodfang, Shadowhowl, Fenris
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70003,100;70108,100;70108,5;70689,5;70690,5' WHERE spawn_point_id = 18;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70003,100;70108,100;70108,5;70689,5;70690,5' WHERE spawn_point_id = 59;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70003,200;70108,5;70689,5;70690,5' WHERE spawn_point_id = 60;

# Lirs Reach: Sunclaw
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70003,180;70108,90;70110,45;71373,1;71374,1;71375,1' WHERE spawn_point_id = 62;

# Shalemont: Connacht Armor bosses
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 331;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 327;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 355;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 397;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 524;

# Shalemont Blademaster Dolan
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70282,250;70289,250;70356,250;142015,148' WHERE spawn_point_id = 356;
```
