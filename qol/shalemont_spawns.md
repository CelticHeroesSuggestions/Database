# Shalemont Ravine Spawns

* What: Spawn point modifications for Shalemont Ravine mobs.
* Why: Several quests are inhibited by the poor spawn rates of certain mobs.
* Notes: N/A
* Changes:
```
# increase spawn rate of Connacht Battleblades
UPDATE ch_live_unitydatadb.spawn_points SET respawn_time = 30, max_respawn_time = 60 WHERE monster_list LIKE '%70311%';

# increase spawn rate of Coldseers
UPDATE ch_live_unitydatadb.spawn_points SET respawn_time = 30, max_respawn_time = 60 WHERE monster_list LIKE '%70357%';

# increase spawn rate of Vanguards
UPDATE ch_live_unitydatadb.spawn_points SET respawn_time = 20, max_respawn_time = 40 WHERE monster_list LIKE '%70354%';
UPDATE ch_live_unitydatadb.spawn_points SET respawn_time = 20, max_respawn_time = 40 WHERE monster_list LIKE '%70353%';
```
