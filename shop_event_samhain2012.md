# Samhain 2012 Event Shops

* What: Spawn points for the Samhain 2012 event shops.
* Why: These shops were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`.
* Notes: I placed the NPCs arbitrarily where it seemed to make sense. I moved the Broom Trader from Farcrag to hang out with Anika (black/red coven hat). The spawn points are compatible with the Samhain 2012 Coven Hat Quest suggestion.
* Changes:
```
# Velkira the Witch (broom trader)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12410, 2, 50, -190.02, 34, 65.84, "stand", "135,1", 1, 90, 50, 0, 0, 0);

# Move her shop from Farcrag to Lirs
UPDATE ch_live_unitydatadb.shop SET zone_id = 2 WHERE npc_id = 135;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 2 WHERE shop_id = 1061;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 2 WHERE shop_id = 1062;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 2 WHERE shop_id = 1063;


# The Wanderer (wraith charms)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12411, 2, 50, 66.32, 10, -62.74, "stand", "250,1", 1, 10, 50, 0, 0, 0);

# Move their shop from Dustwhiter to Lirs
UPDATE ch_live_unitydatadb.shop SET zone_id = 2 WHERE npc_id = 250;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 2 WHERE shop_id = 1064;


# Igor the Crafty (ghoul charms)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12412, 5, 50, -2.62, 10, 33.31, "stand", "133,1", 1, 10, 50, 0, 0, 0);
```
