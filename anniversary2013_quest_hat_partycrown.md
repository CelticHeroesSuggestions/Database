# Party Crowns

* What: Spawn points for the Anniversary 2013 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: Hamish the Hatter (the quest NPC) is located by the tavern.
* Changes:
```
# Hamish the Hatter: see the `anniversary2012_hat_quest_partyhats.md` file for spawning this NPC

# Move the quests to Lirs Reach
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 511;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 512;

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
