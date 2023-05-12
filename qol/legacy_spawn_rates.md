# Legacy Spawn Rates

* What: Increase the spawn chance of certain legacy bosses.
* Why: The content from those bosses is cool, but they are too rare.
* Notes: None.
* Changes:
```
# Lirs Reach: Bloodfang, Shadowhowl, Fenris
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,100,5;70689,5;70690,5' WHERE spawn_point_id = 59;

# Lirs Reach: Sunclaw, Ythair
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70003,180;70108,90;70110,45;71373,1;71374,1;71375,1' WHERE spawn_point_id = 62;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,5;71190,1' WHERE spawn_point_id = 1031;

# Lirs Reach: King Vorum Dreadbone
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;72738,1;72751,1' WHERE spawn_point_id = 1112;

# Shalemont Ravine: Moon Masks
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70262,5;70263,5;70266,5;70268,5;70270,5;70273,5;70637,5;71344,5' WHERE spawn_point_id = 281;

# Shalemont Ravine: Connacht Armor bosses
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 331;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 327;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 355;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 397;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,2000;70679,8;70680,8;70681,8;70686,4;70687,4;70688,4' WHERE spawn_point_id = 524;

# Otherworld: Undead Fire Titan
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;70647,1' WHERE spawn_point_id = 4622;

# Carrowmore Tunnels: Bone Giant
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;70646,1' WHERE spawn_point_id = 5400;

# Various: Witchfinders and Witches
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100010,1;100140,1' WHERE spawn_point_id = 2887;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100022,1;100037,1' WHERE spawn_point_id = 2888;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100024,1;100039,1' WHERE spawn_point_id = 2889;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100023,1;100038,1' WHERE spawn_point_id = 2890;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100025,1;100040,1' WHERE spawn_point_id = 2891;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100026,1;100041,1' WHERE spawn_point_id = 2892;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100027,1;100042,1' WHERE spawn_point_id = 2893;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100019,1;100034,1' WHERE spawn_point_id = 2894;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100020,1;100035,1' WHERE spawn_point_id = 2895;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100021,1;100036,1' WHERE spawn_point_id = 2896;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100031,1;100043,1' WHERE spawn_point_id = 2897;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100032,1;100044,1' WHERE spawn_point_id = 2898;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,10;100033,1;100045,1' WHERE spawn_point_id = 2899;
```
