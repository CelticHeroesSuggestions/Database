# Yuletide 2012: Cloud Mounts

* What: Spawn point for the Yuletide 2012 event shop.
* Why: This shop was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC on the Farcrag Castle parapets, to give more content there.
* Changes:
```
# Skorvan Skycaller (cloud trader)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12500, 93, 50, -10.27, 40, -74.29, "stand", "289,1", 1, 340, 12, 0, 0, 0);

# Move his shop to Farcrag castle
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 93 WHERE shop_id = 11004;

# Remove his quest level requirement
UPDATE ch_live_unitydatadb.quest_templates SET level_required = 1 WHERE quest_id = 463;

# Cloud Spirits (for the quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12501, 93, 50, 6.66, 40, -87.57, "random 5 0 0 1", "73030,1", 1, 340, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12502, 93, 50, 0.96, 40, -87.57, "random 5 0 0 1", "73030,1", 1, 340, 12, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12503, 93, 50, -6.91, 40, -87.57, "random 5 0 0 1", "73030,1", 1, 340, 12, 0, 0, 0);
```
