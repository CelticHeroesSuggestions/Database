# Samhain 2015: Nithsteed Guise

* What: Spawn points for the Samhain 2015 Banshee Blade quest mobs.
* Why: This is a legacy event hat quest that would make a nice re-entrance to the game.
* Notes: I placed the quest NPC (Lochlan Calhoun) in Shalemont Ravine 
* Changes:
```
# Lochlan Calhoun
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15440, 6, 50, 8.8, 0, 17.41, "stand", "138436,1", 1, 355, 50, 0, 0, 0);

# move the quests to Shalemont Ravine
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2163;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2164;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2165;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2166;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2167;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2168;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2169;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2170;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2171;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2172;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2173;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2174;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2175;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2176;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2177;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2178;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2179;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2180;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2181;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2182;

# update the loot tables of the mobs 2287-2292
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2287;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2288;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2289;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2290;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2291;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2292;

# Glaring Terrors
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15441, 6, 10, 19.75, 0, 58.57, "random 5 0 0 1", "138437,2;138440,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15442, 6, 10, 19.75, 0, 58.57, "random 5 0 0 1", "138437,2;138440,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15443, 6, 10, 19.75, 0, 58.57, "random 5 0 0 1", "138437,2;138440,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15444, 6, 10, 19.75, 0, 58.57, "random 5 0 0 1", "138437,2;138440,1", 1, 200, 15, 0, 0, 0);

# Seething Blinders
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15445, 6, 10, 96.53, 0, 69.04, "random 5 0 0 1", "138438,2;138441,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15446, 6, 10, 96.53, 0, 69.04, "random 5 0 0 1", "138438,2;138441,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15447, 6, 10, 96.53, 0, 69.04, "random 5 0 0 1", "138438,2;138441,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15448, 6, 10, 96.53, 0, 69.04, "random 5 0 0 1", "138438,2;138441,1", 1, 200, 15, 0, 0, 0);

# Mind Borers
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15449, 6, 10, 7.37, 0, -55.43, "random 5 0 0 1", "138439,2;138442,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15450, 6, 10, 7.37, 0, -55.43, "random 5 0 0 1", "138439,2;138442,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15451, 6, 10, 7.37, 0, -55.43, "random 5 0 0 1", "138439,2;138442,1", 1, 200, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15452, 6, 10, 7.37, 0, -55.43, "random 5 0 0 1", "138439,2;138442,1", 1, 200, 15, 0, 0, 0);
```
