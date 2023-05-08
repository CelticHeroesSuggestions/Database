# Beltane 2013: Mount (Dragonstaff) Shop

* What: Spawn point for the Beltane 2013 event shop.
* Why: The mounts from this shop were fun and would be a nice revival for the game.
* Notes: I placed the NPC at Stonevale's Northern Woods, to give more content there.
* Changes:
```
# Samrad the Wizard
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13301, 3, 50, 256.98, 0, -188.98, "stand", "372,1", 1, 120, 12, 0, 0, 0);

# Move his shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 10020;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 10020;
```
