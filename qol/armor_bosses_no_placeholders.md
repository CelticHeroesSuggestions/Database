# Removing Placeholders from Quest Armor Bosses

* What: Removed 4s placeholders from Warden, Meteoric, Frozen, Dragonlord, and Exalted Dragonlord bosses.
* Why: The 4s placeholders are a waste of time and cause bottlenecks for gear.
* Notes: None.
* Changes:
```
# Warden
# Fellfire
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70600,1;70667,3' WHERE spawn_point_id = 496;
# Chillmist
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70601,1;70668,3' WHERE spawn_point_id = 498;
# Starspell
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70602,1;70669,3' WHERE spawn_point_id = 497;
# Spirehoof
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70603,1;70670,3' WHERE spawn_point_id = 468;
# Falgren
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70604,1;70671,3' WHERE spawn_point_id = 495;

# Meteoric
# Stonefang
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70717,50;70778,50;70788,8' WHERE spawn_point_id = 625;
# Bonehead
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70718,50;70779,50;70789,8' WHERE spawn_point_id = 621;
# Goretusk
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70712,50;70773,50;70783,8' WHERE spawn_point_id = 624;
# Bladewing
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70713,50;71774,50;70784,8' WHERE spawn_point_id = 623;
# Spearhorn
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70715,50;70776,50;70786,8' WHERE spawn_point_id = 622;
# Coppinger
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70716,50;70777,50;70787,8' WHERE spawn_point_id = 2674;
# Ironscale
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70719,50;70780,50;70790,8' WHERE spawn_point_id = 2311;
# Shivercowl
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70720,50;70781,50;70791,8' WHERE spawn_point_id = 2348;
# Rockbelly
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70721,50;70782,50;70792,8' WHERE spawn_point_id = 620;

```
