# Shalemont Ravine Spawns

* What: Spawn point modifications for Stonevale mobs.
* Why: Several quests are inhibited by the poor spawn rates of certain mobs.
* Notes: N/A
* Changes:
```
# increase spawn chance and rate of Frenzied Bears
UPDATE ch_live_unitydatadb.spawn_points SET respawn_time = 30, max_respawn_time = 60, monster_list = '100270,1' WHERE spawn_point_id = 4628;
```
