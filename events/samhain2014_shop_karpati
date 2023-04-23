# Samhain 2014: Luxury Shop

* What: Spawn point for the Samhain 2014 luxury event shop.
* Why: This shop was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC at Shalemont's river leystone, to give more content there.
* Changes:
```
# Miruna of the Karpati (jewelry shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14400, 6, 50, 3.98, 0, 5.22, "stand", "875,1", 1, 160, 12, 0, 0, 0);

# Move her shop to Shalemont
UPDATE ch_live_unitydatadb.shop SET zone_id = 6 WHERE shop_id = 12003;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 6 WHERE shop_id = 12003;

# Cornel of the Karpati (mount shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14401, 6, 50, 1.96, 0, 7.26, "stand", "874,1", 1, 110, 12, 0, 0, 0);

# Move his shop to Shalemont
UPDATE ch_live_unitydatadb.shop SET zone_id = 6 WHERE shop_id = 12004;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 6 WHERE shop_id = 12004;
```
