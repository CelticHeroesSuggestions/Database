# Yuletide 2013: Frost Items (Frostgloves, Frostboots, etc)

* What: Spawn points for the Yuletide 2013 gear quest
* Why: This gear was surprisingly good for its time, and would make a nice re-entrance.
* Table: `ch_live_unitydatadb.spawn_points`.
* Notes: The gear quest NPCs are at Southern Road, inauthentically placed.
* Changes:
```
# Sergeant Cairn (Frost Items quest), has broken dialogue (uses one of the Heroes Landing guards for some reason)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13521, 93, 1, -7.48, 0, 0.66, "stand", "807,1", 1, 45, 2, 0, 0, 0);


# Iona (Candy Cane quest), has broken dialogue (uses one of the Heroes Landing guards for some reason)
#INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
#VALUES (13520, 2, 1, -89.57, 0, -272.04, "stand", "808,1", 1, 280, 2, 0, 0, 0);
```
