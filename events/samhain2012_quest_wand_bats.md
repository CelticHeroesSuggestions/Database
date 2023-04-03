# Cane of Bats

* What: Spawn points for the Samhain 2012 event wand quest NPCs and mobs.
* Why: This is a legacy event wand quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`.
* Notes: The NPC for this quest was also the NPC for the Wand of Hallows (Samhain 2011) and Snowball Wand (Yuletide 2011). Therefore the quests for those items are unavailable unless they can be patched into another NPC.
* Changes:
```
# Festus the Mad
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12420, 9, 50, 23.66, 5, 46.87, "stand", "140,1", 1, 240, 50, 0, 0, 0);

# Make the quest available
UPDATE ch_live_unitydatadb.quest_templates SET level_required = 1 WHERE quest_id = 407;
UPDATE ch_live_unitydatadb.quest_templates SET level_required = 1 WHERE quest_id = 408;

# spawn a Cave Bat
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12421, 9, 20, -23.92, 5, -41.17, "random 5 0 0 1", "72744,1", 1, 165, 30, 0, 0, 0);

# spawn a Black Bat
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12422, 9, 20, -20.02, 5, -38.98, "random 5 0 0 1", "72745,1", 1, 165, 30, 0, 0, 0);

# spawn a Vampire Bat
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12423, 9, 20, -22.03, 5, -32.88, "random 5 0 0 1", "72746,1", 1, 165, 30, 0, 0, 0);

# spawn a Cave Bat
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12424, 9, 20, -23.92, 5, -41.17, "random 5 0 0 1", "72744,1", 1, 165, 30, 0, 0, 0);

# spawn a Black Bat
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12425, 9, 20, -20.02, 5, -38.98, "random 5 0 0 1", "72745,1", 1, 165, 30, 0, 0, 0);

# spawn a Vampire Bat
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12426, 9, 20, -22.03, 5, -32.88, "random 5 0 0 1", "72746,1", 1, 165, 30, 0, 0, 0);

# spawn a Samhain Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12427, 5, 20, 27.73, 5, -73.28, "random 5 0 0 1", "72747,1", 1, 270, 30, 0, 0, 0);

# spawn a Samhain Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12428, 5, 20, 0, 5, -44.63, "random 5 0 0 1", "72747,1", 1, 270, 30, 0, 0, 0);
```
