# Samhain 2015: Banshee Blades

* What: Spawn points for the Samhain 2015 Banshee Blade quest mobs.
* Why: This is a legacy event quest that would make a nice re-entrance to the game.
* Notes: I placed the quest NPC (Sabrina MacDonald) in Shalemont Ravine 
* Changes:
```
# Sabrina MacDonald
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15402, 6, 50, 6.42, 0, 17.55, "stand", "138548,1", 1, 40, 50, 0, 0, 0);

# Move the quests to Shalemont Ravine
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2232;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2233;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2234;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2235;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2236;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2237;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2158;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2159;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2160;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2161;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 6 WHERE quest_id = 2162;

# Savage Skeletons
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15411, 6, 15, 42.9, 0, 22.17, "random 10 0 0 1", "138523,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15412, 6, 15, 42.9, 0, 22.17, "random 10 0 0 1", "138523,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15413, 6, 15, 42.9, 0, 22.17, "random 10 0 0 1", "138523,1", 1, 200, 30, 0, 0, 0);

# Entombed Bloodshank
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15414, 6, 15, -16.87, 0, 22.19, "random 10 0 0 1", "138524,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15415, 6, 15, -16.87, 0, 22.19, "random 10 0 0 1", "138524,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15416, 6, 15, -16.87, 0, 22.19, "random 10 0 0 1", "138524,1", 1, 200, 30, 0, 0, 0);

# Blood Moon Reaper
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15417, 6, 15, 137.5, 0, 90.1, "random 10 0 0 1", "138525,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15418, 6, 15, 137.5, 0, 90.1, "random 10 0 0 1", "138525,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15419, 6, 15, 137.5, 0, 90.1, "random 10 0 0 1", "138525,1", 1, 200, 30, 0, 0, 0);

# Savage Bone Lord
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15420, 6, 15, 193.01, 0, 129.95, "random 10 0 0 1", "138526,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15421, 6, 15, 193.01, 0, 129.95, "random 10 0 0 1", "138526,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15422, 6, 15, 193.01, 0, 129.95, "random 10 0 0 1", "138526,1", 1, 200, 30, 0, 0, 0);

# Entombed Bone Lord
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15423, 6, 15, 168.07, 0, 173.06, "random 10 0 0 1", "138527,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15424, 6, 15, 168.07, 0, 173.06, "random 10 0 0 1", "138527,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15425, 6, 15, 168.07, 0, 173.06, "random 10 0 0 1", "138527,1", 1, 200, 30, 0, 0, 0);

# Blood Moon Bone Lord
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15426, 6, 15, -37.35, 0, 116.42, "random 10 0 0 1", "138528,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15427, 6, 15, -37.35, 0, 116.42, "random 10 0 0 1", "138528,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15428, 6, 15, -37.35, 0, 116.42, "random 10 0 0 1", "138528,1", 1, 200, 30, 0, 0, 0);

# increase the number of powder drops
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2380;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2381;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2382;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2383;
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 10 WHERE loot_table_id = 2384;

# Signal Fire
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15429, 2, 15, -227.65, 0, -37.39, "stand", "138542,1", 1, 200, 30, 0, 0, 0);

# Beacon Fire
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15430, 2, 15, 248.79, 0, -239.5, "stand", "138543,1", 1, 200, 30, 0, 0, 0);

# Guiding Fire
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15431, 2, 15, 78.4, 0, -78.85, "stand", "138544,1", 1, 200, 30, 0, 0, 0);
```

Update `mob_data.txt` to set the Signal Fire mob to a barrel
```
...
138542,51219,0.3,Signal Fire Barrel,2800,0,0,-1,23,0,1,2,0,0,1
...
```
