# Yuletide 2015: Luxury Shop

* What: Spawn point for the Yuletide 2015 luxury event shop.
* Why: This shop was very popular and would be a nice revival for the game.
* Notes: I placed the NPC at Shalemont's river leystone, to give more content there.
* Changes:
```
# Kristen Greenleaf (jewelry shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15500, 93, 50, 0.74, 0, -34.11, "stand", "892,1", 1, 315, 12, 0, 0, 0);

# Move her shop to Farcrag Castle
UPDATE ch_live_unitydatadb.shop SET zone_id = 93 WHERE shop_id = 1094;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 93 WHERE shop_id = 1094;

# Rorak Falstaff (mount shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15501, 93, 50, -1.8, 0, -34.11, "stand", "889,1", 1, 45, 12, 0, 0, 0);

# Move his shop to Farcrag Castle
UPDATE ch_live_unitydatadb.shop SET zone_id = 93 WHERE shop_id = 12004;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 93 WHERE shop_id = 12004;
```
