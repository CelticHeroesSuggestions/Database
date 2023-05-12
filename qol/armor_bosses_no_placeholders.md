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

# Frozen
# Eye
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71055,10;71223,10;71251,10' WHERE spawn_point_id = 988;
# Kelpie
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71054,10;71224,10;71252,10' WHERE spawn_point_id = 704;
# Ghost
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71052,10;71226,10;71253,10' WHERE spawn_point_id = 882;
# Woodcrown
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71053,10;71225,10;71254,10' WHERE spawn_point_id = 881;
# Grey Golem
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71051,10;71227,10;71255,10' WHERE spawn_point_id = 880;
# Lava Golem
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71050,10;71228,10;71256,10' WHERE spawn_point_id = 878;

# Dragonlord
# 150 Wyvern
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71857,1;71858,1' WHERE spawn_point_id = 1503;
# 155 Spider
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71860,1;71861,1' WHERE spawn_point_id = 1504;
# 160 Boggan
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71863,1;71864,1' WHERE spawn_point_id = 1505;
# 165 Boggan
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71866,1;71867,1' WHERE spawn_point_id = 1506;
# 170 Firbolg
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71869,1;71870,1' WHERE spawn_point_id = 1507;
# 180 Troll
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '71872,1;71873,1' WHERE spawn_point_id = 1508;

# Exalted Dragonlord
# 185 Curr
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103006,1;103007,1' WHERE spawn_point_id = 3059;
# 190 Wizard
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103009,1;103010,1' WHERE spawn_point_id = 3254;
# 195 Automaton
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103012,1;103013,1' WHERE spawn_point_id = 3398;
# 200 Imp
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103015,1;103016,1' WHERE spawn_point_id = 3420;
# 205 Hexwyrm
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103018,1;103019,1' WHERE spawn_point_id = 3624;
# 210 Automaton
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103021,1;103022,1' WHERE spawn_point_id = 3625;
# 215 Eye
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '103024,1;103025,1' WHERE spawn_point_id = 3787;
```
