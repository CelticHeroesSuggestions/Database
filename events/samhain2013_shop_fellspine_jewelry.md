# Samhain 2013: Fellspine and Jewelry Shop

* What: Spawn point for the Samhain 2011 event shop.
* Why: This shop was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop`.
* Notes: I placed the NPC in Farcrag Castle (next to the novelty trainer) to give more content there.
* Changes:
```
# spawn the NPC in farcrag, next to the novelty trainer
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11400, 93, 50, 57.09, 40, -79.58, "stand", "100006,1", 1, 275, 12, 0, 0, 0);

# make the shop accessible from this NPC
UPDATE ch_live_unitydatadb.shop SET npc_id = 100006 WHERE shop_id = 12000;

# the shop is accessible from Farcrag by default, so no other changes are necessary
```
