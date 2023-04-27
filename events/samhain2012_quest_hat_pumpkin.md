# Samhain 2012: Pumpkin Helmet

* What: Spawn points for the Samhain 2012 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed the Quest NPC near Highshore, with the Halloween shop.
* Changes:
```
# Morvern Pumpkinhead
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12408, 2, 50, -191.15, 0, 68.60, "stand", "134,1", 1, 105, 12, 0, 0, 0);

# Move the quest to Lirs
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 95;

# Remove the prerequisite quests, which no longer exist
DELETE FROM ch_live_unitydatadb.quest_prerequesits WHERE quest_id = 95;

# Add some Pumpkinheads west of Morvern Pumpkinhead
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12430, 2, 10, -200.26, 0, 82.73, "random 5 0 0 1", "70648,1", 1, 105, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12431, 2, 10, -205.51, 0, 81.63, "random 5 0 0 1", "70648,1", 1, 105, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12432, 2, 10, -208.68, 0, 88.26, "random 5 0 0 1", "70648,1", 1, 105, 20, 0, 0, 0);
```
