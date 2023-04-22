# Nature Masks

* What: Spawn points for the Beltane 2014 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: The Green Man (the quest NPC) is located at Stonevale's Northern Woods.
* Changes:
```
# The Green Man
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14301, 3, 50, 189.4, 0, 170.55, "stand", "100221,1", 1, 273, 12, 0, 0, 0);

# Move the quests to Stonevale
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1436;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1437;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1438;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1439;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1440;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1441;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1442;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1443;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1444;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1445;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1446;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1447;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1448;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1449;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1450;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1451;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1452;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1453;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1454;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1455;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1456;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1457;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1458;


# Tor Caith Faeries (boar pit)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14302, 3, 50, 206.73, 0, 113.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14303, 3, 50, 208.73, 0, 113.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14304, 3, 50, 210.73, 0, 113.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14305, 3, 50, 212.73, 0, 113.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14306, 3, 50, 206.73, 0, 117.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14307, 3, 50, 208.73, 0, 117.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14308, 3, 50, 210.73, 0, 117.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14309, 3, 50, 212.73, 0, 117.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14310, 3, 50, 206.73, 0, 105.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14311, 3, 50, 208.73, 0, 105.26, "random 5 0 0 1", "100200,1", 1, 273, 12, 0, 0, 0);

```
