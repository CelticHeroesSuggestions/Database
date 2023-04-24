# Ostara 2016 Hat (Trapper's Cap) quests

* What: Spawn points for the Ostara 2016 event quest.
* Why: This quest was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed the NPCs near Stonevale Farm to give more content there.
* Changes:
```
# Afallon the Hunter (hat)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16100, 3, 50, 43.12, 0, -37.32, "stand", "101162,1", 1, 135, 12, 0, 0, 0);

# move his quests to stonevale
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1738;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1739;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1740;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1741;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1742;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1743;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1744;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1745;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1746;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1747;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1748;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1749;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1750;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1751;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1752;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1753;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1754;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1755;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1756;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1757;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 3 WHERE quest_id = 1758;

# spawn the snakes
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16110, 3, 10, 52.74, 0, -31.39, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16111, 3, 10, 52.74, 0, -31.39, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16112, 3, 10, 52.74, 0, -31.39, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16113, 3, 10, 52.74, 0, -31.39, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16114, 3, 10, 52.74, 0, -31.39, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);

INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16115, 3, 10, 59.47, 0, -37.25, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16116, 3, 10, 59.47, 0, -37.25, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16117, 3, 10, 59.47, 0, -37.25, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16118, 3, 10, 59.47, 0, -37.25, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16119, 3, 10, 59.47, 0, -37.25, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);

INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16120, 3, 10, 57.33, 0, -34.68, "random 10 0 0 1", "101177,1;101178,1;101179,1;101180,1", 1, 45, 15, 0, 0, 0);
```
