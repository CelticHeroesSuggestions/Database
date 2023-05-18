# Dustwither Catacombs Boss Balancing

* What: Update the three Dustwither Catacombs boss spawns and loot tables.
* Why: The bosses are essential for certain gear drops, however that gear is very rare.
* Notes: N/A
* Changes:
```
# Guarantee 6* spawns at those points
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70199,1' WHERE spawn_point_id = 197;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70200,1' WHERE spawn_point_id = 198;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70201,1' WHERE spawn_point_id = 199;

# Increase drop count to 5
UPDATE ch_live_unitydatadb.mob_loot_sets SET num_drops = 5 WHERE mob_template_id = 70199;
UPDATE ch_live_unitydatadb.mob_loot_sets SET num_drops = 5 WHERE mob_template_id = 70200;
UPDATE ch_live_unitydatadb.mob_loot_sets SET num_drops = 5 WHERE mob_template_id = 70201;
```
