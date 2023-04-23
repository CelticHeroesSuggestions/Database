# Ostara 2015 Jewelry and Phoenixes

* What: Spawn points for the Ostara 2015 event shops.
* Why: These shops were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPCs near Stonevale Farm to give more content there.
* Changes:
```
# Gayle the Hunter (jewelry trader)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15101, 3, 50, 90.32, 40, -67.50, "stand", "878,1", 1, 340, 12, 0, 0, 0);

# Move her shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 1081;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 1081;

# Raghnall the Hunter (phoenix mount trader)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15102, 3, 50, 92.16, 40, -68.80, "stand", "879,1", 1, 300, 12, 0, 0, 0);

# Move his shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 15025;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 15025;
```
