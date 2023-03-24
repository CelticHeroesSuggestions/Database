# Party Hats

* What: Spawn points for the Anniversary 2012 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed the NPCs roughly where the instructions say they are. The green presents are in Farcrag Castle (by the fountain), and the red presents are in Lirs (around the Tavern). Since lots of hat quests use presents, this quest is set to (inauthentically) use the Anniversary 2013 presents. ALSO, due to Hamish the Hatter being recycled for the 2013 anniversary hat quest (party crowns), this quest is not available unless the hatman's XML file is modified.
* Changes:
```
# Hamish the Hatter
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12202, 2, 50, 254.30, 0, -250.58, "stand", "379,1", 1, 300, 50, 0, 0, 0);

# Move the quests to Lirs Reach
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 328;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 330;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 331;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 332;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 333;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 334;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 335;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 336;

# Change the quests to use 2013 presents
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35274,5' WHERE quest_id = 328 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35274,5' WHERE quest_id = 328 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,10' WHERE quest_id = 330 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,10' WHERE quest_id = 330 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,20' WHERE quest_id = 331 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,20' WHERE quest_id = 331 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,50' WHERE quest_id = 332 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,50' WHERE quest_id = 332 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,100' WHERE quest_id = 333 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,100' WHERE quest_id = 333 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,150' WHERE quest_id = 334 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,150' WHERE quest_id = 334 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,250' WHERE quest_id = 335 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,250' WHERE quest_id = 335 AND stage_id = 1;

# Red Present Spawns (Farcrag)
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12201, 93, 30, -27.5, -100, -29.14, "35274,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12202, 93, 30, -28.15, -100, -18.48, "35274,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12203, 93, 30, -27.19, -100, -10.71, "35274,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12204, 93, 30, -24.68, -100, -5.06, "35274,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12205, 93, 30, -13.96, -100, 0.68, "35274,100", 45);

# Green Present Spawns (Lirs)
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12210, 2, 30, 262.51, 0, -260.78, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12211, 2, 30, 254.70, 0, -262.18, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12212, 2, 30, 263.22, 0, -241.87, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12213, 2, 30, 254.29, 0, -237.5, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12214, 2, 30, 247.16, 0, -257.28, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12215, 2, 30, 236.35, 0, -257.27, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12216, 2, 30, 234.32, 0, -262.45, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12217, 2, 30, 225.51, 0, -268.01, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12218, 2, 30, 219.2, 0, -266.43, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12219, 2, 30, 238.11, 0, -266.14, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12220, 2, 30, 236.19, 0, -259.14, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12221, 2, 30, 247.50, 0, -261.34, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12222, 2, 30, 251.99, 0, -259.08, "35275,100", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12223, 2, 30, 250.1, 0, -266.26, "35275,100", 45);
```
