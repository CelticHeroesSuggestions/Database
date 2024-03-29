# Beltane 2015 Wand (Shillelagh) and Hat (Visage) quests

* What: Spawn points for the Beltane 2015 event quests.
* Why: These quests were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed the NPCs near Stonevale Farm to give more content there.
* Changes:
```
# Sage Padriga (wand)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15303, 3, 50, 91.37, 0, -82.70, "stand", "138419,1", 1, 210, 12, 0, 0, 0);

# move quests to Stonevale
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1990;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1991;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1994;

# Spawns for Faerie of Dust, Faerie of Grime, Faerie of Ashes, and Trasgar of Cinereal
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15310, 3, 10, 77.78, 0, -101.55, "random 10 0 0 1", "138422,1", 1, 45, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15311, 3, 10, 52.78, 0, -105.74, "random 10 0 0 1", "138423,1", 1, 45, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15312, 3, 10, 44.45, 0, -89.67, "random 10 0 0 1", "138424,1", 1, 45, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15313, 3, 15, 60.54, 0, -66.35, "stand", "138421,1", 1, 0, 30, 0, 0, 0);


# Sage Erwana (hat)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15304, 3, 50, 93.99, 0, -79.83, "stand", "138398,1", 1, 250, 12, 0, 0, 0);

# move quests to Stonevale
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1786;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1787;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1788;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1789;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1790;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1791;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1792;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1793;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1794;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1795;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1796;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1797;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1798;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1799;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1800;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1801;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1802;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1803;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1804;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1805;

# Spawns for flowers
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15301, 3, 15, 70.09, 0, -64.31, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15302, 3, 15, 76.7, 0, -63.68, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15303, 3, 15, 85.63, 0, -65.56, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15304, 3, 15, 93.54, 0, -82.23, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15305, 3, 15, 91.29, 0, -86.04, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15306, 3, 15, 89.76, 0, -92.53, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15307, 3, 15, 88.98, 0, -97.32, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15308, 3, 15, 93.43, 0, -102.68, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15309, 3, 15, 85.43, 0, -112.88, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15310, 3, 15, 75.89, 0, -118.74, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15311, 3, 15, 66.70, 0, -105.31, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15312, 3, 15, 69.25, 0, -89.09, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15313, 3, 15, 73.65, 0, -80.63, "54958,570;54959,200;54960,70", 30);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (15314, 3, 15, 64.40, 0, -74.11, "54958,570;54959,200;54960,70", 30);


# Sage Conroy (lore)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15305, 3, 50, 94.31, 20, -73.02, "stand", "138399,1", 1, 300, 12, 0, 0, 0);
```
