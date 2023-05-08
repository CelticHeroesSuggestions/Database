# Garlands

* What: Spawn points for the Beltane (Midsummer) 2013 event hat quest NPCs and items.
* Why: Garlands did not make a reappearance after 2013 and would be a nice readdition.
* Notes: I placed the quest NPC (Talwen the Weaver) at roughly her original spot in Highshore Village.
* Changes:

```
# Talwen the Weaver
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13330, 2, 50, -113.05, 0, -11.19, "stand", "378,1", 1, 90, 50, 0, 0, 0);

# move the quests to Lirs Reach (they should already be there by default)
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 515;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 516;

# update the garland rewards for an equal garland split
UPDATE ch_live_unitydatadb.loot_table_items SET weight = 1 WHERE loot_table_id = 1650;

# Poppy
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13331, 2, 10, -81.41, 0, -9.58, "35413,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13332, 2, 10, -83.46, 0, 4.11, "35413,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13333, 2, 10, -64.02, 0, -12.61, "35413,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13334, 2, 10, -61.62, 0, 9.74, "35413,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13335, 2, 10, -85.91, 0, 11.21, "35413,1", 20);

# Foxglove
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13336, 2, 10, -84.41, 0, -3.65, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13337, 2, 10, -69.2, 0, -9.4, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13338, 2, 10, -64.51, 0, 2.34, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13339, 2, 10, -52.64, 0, -5.61, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13340, 2, 10, -50.31, 0, -13.8, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13341, 2, 10, -39.2, 0, -5.73, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13342, 2, 10, -41.66, 0, 1.24, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13343, 2, 10, -28.00, 0, -0.77, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13344, 2, 10, -25.93, 0, -13.23, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13345, 2, 10, -34.73, 0, -17.28, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13346, 2, 10, -41.12, 0, -21.60, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13347, 2, 10, -49.24, 0, 25.16, "35414,1", 20);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (13348, 2, 10, -51.57, 0, -18.95, "35414,1", 20);
```
