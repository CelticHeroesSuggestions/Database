# Beltane 2014: Luxury Shop

* What: Spawn point for the Beltane 2014 event shop.
* Why: This shop was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC at Stonevale's Northern Woods, to give more content there.
* Changes:
```
# Rowan of Ardmair (luxury shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14300, 3, 50, 188.84, 0, 168.36, "stand", "860,1", 1, 273, 12, 0, 0, 0);

# Move his shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 12002;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 12002;
```
