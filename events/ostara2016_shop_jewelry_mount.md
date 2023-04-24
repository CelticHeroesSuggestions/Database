# Ostara 2016 Shops

* What: Spawn points for the Ostara 2016 shops.
* Why: These shops were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed the NPCs near Stonevale Farm to give more content there.
* Changes:
```
# Caitlin the Hunter (jewelry)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16101, 3, 50, 45.42, 0, -38.17, "stand", "101540,1", 1, 180, 12, 0, 0, 0);

# move her shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 1098;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 1098;

# Raghnall the Hunter (mount)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (16102, 3, 50, 92.16, 40, -68.80, "stand", "879,1", 1, 300, 12, 0, 0, 0);

# Move his shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 15025;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 15025;
```
