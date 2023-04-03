# Carpets

* What: Spawn points for the Beltane 2012 event shops.
* Why: This shop was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC on the Farcrag Castle parapets to give more content there.
* Changes:
```
# Rasool the Mystic (carpet trader)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12302, 93, 50, -12.82, 40, -74.43, "stand", "203,1", 1, 20, 12, 0, 0, 0);

# Add a white carpet to the black carpet shop (for lack of a better shop to put in)
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order) VALUES (1028, 93, 20550, -1, 0)
```
