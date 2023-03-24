# Yuletide 2012: Tempest Spirit

* What: Spawn points for the Yuletide 2012 Tempest Spirit and Snowstorm Spirits
* Why: This mob dropped a cool wand that is currently unavailable, and snowballs are a fun novelty.
* Table: `ch_live_unitydatadb.spawn_points`.
* Notes: I placed the Tempest Spirit in the Highshore Village field, where it was originally located. I placed the Snowstorm Spirits around the Tempest Spirit to keep the encounter a little more vibrant and contained.
* Changes:
```
# Tempest Spirit
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12520, 2, 1800, -33.33, 0, 15.01, "random 5 0 0 1", "72845,1", 1, 0, 1860, 0, 0, 0);

# Snowstorm Spirit (had rare chance at clouds, dropped snowballs)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12521, 2, 60, -43.57, 0, 24.93, "random 5 0 0 1", "73056,1", 1, 0, 90, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12522, 2, 60, -31.5, 0, 25.27, "random 5 0 0 1", "73056,1", 1, 0, 90, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12523, 2, 60, -25.55, 0, 18.80, "random 5 0 0 1", "73056,1", 1, 0, 90, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12524, 2, 60, -24.2, 0, 8.24, "random 5 0 0 1", "73056,1", 1, 0, 90, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12525, 2, 60, -42.52, 0, 9.67, "random 5 0 0 1", "73056,1", 1, 0, 90, 0, 0, 0);
```
