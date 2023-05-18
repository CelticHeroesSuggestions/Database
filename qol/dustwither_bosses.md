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
UPDATE ch_live_unitydatadb.mob_templates SET num_drops = 5 WHERE mob_template_id = 70199;  # formerly 1
UPDATE ch_live_unitydatadb.mob_templates SET num_drops = 5 WHERE mob_template_id = 70200;  # formerly 1
UPDATE ch_live_unitydatadb.mob_templates SET num_drops = 5 WHERE mob_template_id = 70201;  # formerly 1

# Reduce boss damage
UPDATE ch_live_unitydatadb.mob_templates SET damage_list = '1,20' WHERE mob_template_id = 70199;  # formerly '1,186'
UPDATE ch_live_unitydatadb.mob_templates SET damage_list = '1,25' WHERE mob_template_id = 70200;  # formerly '1,212'
UPDATE ch_live_unitydatadb.mob_templates SET damage_list = '1,30' WHERE mob_template_id = 70201;  # formerly '1,238'

# Reduce boss health
UPDATE ch_live_unitydatadb.mob_templates SET hitpoints = 5000 WHERE mob_template_id = 70199;  # formerly 16544
UPDATE ch_live_unitydatadb.mob_templates SET hitpoints = 6000 WHERE mob_template_id = 70200;  # formerly 18784
UPDATE ch_live_unitydatadb.mob_templates SET hitpoints = 7000 WHERE mob_template_id = 70201;  # formerly 21024

# Reduce boss resists
UPDATE ch_live_unitydatadb.mob_templates SET resistance_list = '3,150;4,150;5,150' WHERE mob_template_id = 70199;  # formerly '3,240;4,240;5,240'
UPDATE ch_live_unitydatadb.mob_templates SET resistance_list = '3,150;4,150;5,150' WHERE mob_template_id = 70200;  # formerly '3,280;4,280;5,280'
UPDATE ch_live_unitydatadb.mob_templates SET resistance_list = '3,150;4,150;5,150' WHERE mob_template_id = 70201;  # formerly '3,320;4,320;5,320'

```
