# Beltane 2015 Shops

* What: Spawn points for the Beltane 2015 event shops.
* Why: These shops were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPCs near Stonevale Farm to give more content there.
* Changes:
```
# Sage Caradoc (jewelry)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15306, 3, 50, 89.47, 0, -82.53, "stand", "884,1", 1, 160, 12, 0, 0, 0);

# Move his shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 1083;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 1083;


# Sage Galena (capes)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15307, 3, 50, 93.99, 0, -77.86, "stand", "885,1", 1, 290, 12, 0, 0, 0);

# Move her shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 1084;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 1084;
```
