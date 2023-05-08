# Beltane 2013: Summer Bears

* What: Spawn point for the Beltane 2013 summer bears.
* Why: These bears were removed from the game and would be a nice readdition.
* Notes: I placed the bears at their original locations.
* Changes:
```
# Steelfang/Sunpaw
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13302, 2, 1800, 154.04, 0, -275.28, "random 5 0 0 1", "74050,1;74053,1", 1, 120, 3600, 0, 0, 0);

# Emberfang
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13303, 2, 1800, -82.06, 0, -75.61, "random 5 0 0 1", "74049,1", 1, 120, 3600, 0, 0, 0);

# Summerclaw
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13304, 2, 1800, -253.19, 0, -6.28, "random 5 0 0 1", "74048,1", 1, 120, 3600, 0, 0, 0);
```
