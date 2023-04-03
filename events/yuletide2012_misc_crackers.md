# Yuletide 2012: Crackers

* What: Spawn points for the Yuletide 2012 cracker consumables.
* Why: The crackers were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.item_spawns`
* Notes: The crackers are in the tavern. The spawn rates are arbitrary.
* Changes:
```
# spawn a few crackers in the Tavern, the 30 series is used to avoid potential conflicts with item IDs
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12530, 9, 30, -0.35, 0, 51.42, "22617,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12531, 9, 30, -12.41, 0, 44.09, "22619,1", 45);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12532, 9, 30, -13.25, 0, 31.81, "22620,1", 45);
```
