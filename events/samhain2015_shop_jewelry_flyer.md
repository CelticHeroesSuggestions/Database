# Samhain 2015: Luxury and Mount Shops

* What: Spawn points for the Samhain 2015 event shops.
* Why: These shops were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC at Dustwither Catacomb's Withered Vaults leystone, to give more content there.
* Changes:
```
# Seonaid Ashcroft (jewelry shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15400, 5, 50, -9.31, 0, -93.99, "stand", "400,1", 1, 30, 12, 0, 0, 0);

# Move his shop to Dustwither Catacombs
UPDATE ch_live_unitydatadb.shop SET zone_id = 5 WHERE shop_id = 12009;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 5 WHERE shop_id = 12009;

# Telor Stewart (mount shop)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15401, 5, 50, -11.98, 0, -96.79, "stand", "888,1", 1, 70, 12, 0, 0, 0);

# Move his shop to Dustwither Catacombs
UPDATE ch_live_unitydatadb.shop SET zone_id = 5 WHERE shop_id = 1085;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 5 WHERE shop_id = 1085;
```
