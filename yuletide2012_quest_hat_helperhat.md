# Yuletide Helper Hats

* What: Spawn points for the Yuletide 2012 event hat quest NPC.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points``.
* Notes: I placed The Yulefather in Farcrag Castle near the skill trainers. I also changed the present to use the (inauthentic) 2014 Yule Presents since the name is nicer and it would be nice to use the same present for all such quests.
* Changes:
```
# The Yulefather
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12530, 93, 10, 84.94, 0, -20.63, "stand", "141,1", 1, 265, 50, 0, 0, 0);

# Move the quests to Farcrag Castle
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 459;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 460;

# Update the present used in the quests
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 459 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 459 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 460 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 460 AND stage_id = 1;

# Place the red presents near The Yulefather, uses the 2014 yuletide present
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12500, 93, 30, 87.76, -80, -14.90, "53341,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12501, 93, 30, 91.88, -80, -17.85, "53341,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12502, 93, 30, 89.64, -80, -23.13, "53341,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12503, 93, 30, 82.36, -80, -29.12, "53341,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12504, 93, 30, 77.85, -80, -24.05, "53341,1", 45);

# Place the green presents near the skill vendors (room adjacent to the Yulefather), uses the 2012 yuletide present (the 2014 model has a better name but the 3D object is a chest, not a present)
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12505, 93, 30, 77.16, -80, -1.79, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12506, 93, 30, 81.91, -80, 2.51, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12507, 93, 30, 76.93, -80, 1.15, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12508, 93, 30, 75.5, -80, 10.97, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12509, 93, 30, 69.11, -80, 19.49, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12510, 93, 30, 64.20, -80, 20.09, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12511, 93, 30, 60.5, -80, 14.79, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12512, 93, 30, 53.12, -80, 11.85, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12513, 93, 30, 52.07, -80, 7.93, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12514, 93, 30, 45.75, -80, 7.19, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12515, 93, 30, 49.49, -80, -3.21, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12516, 93, 30, 56.45, -80, -9.55, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12517, 93, 30, 63.42, -80, -14.60, "22588,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12518, 93, 30, 65.94 -80, -9.49, "22588,1", 45);
```
