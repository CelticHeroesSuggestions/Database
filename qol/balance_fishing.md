# Balancing Fishing

* What: Balances fishing for solo play.
* Why: Drop rates of certain fishing items and spawns is too low.
* Notes: N/A
* Changes:
```
# remove Glacial Waters: the spawns are normal spawns followed by the various Glacial spawns, so can safely only include the spawns left of the first '141690' 
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = left(monster_list, locate('141690', monster_list) - 1) WHERE (
  monster_list LIKE '%141690%' OR
  monster_list LIKE '%141691%' OR
  monster_list LIKE '%141692%' OR
  monster_list LIKE '%141693%' OR
  monster_list LIKE '%141694%' OR
  monster_list LIKE '%141695%' OR
  monster_list LIKE '%141696%' OR
  monster_list LIKE '%141697%' OR
  monster_list LIKE '%141698%' OR
  monster_list LIKE '%141699%' OR
  monster_list LIKE '%141700%' OR
  monster_list LIKE '%141701%' OR
  monster_list LIKE '%141702%' OR
  monster_list LIKE '%141703%' OR
  monster_list LIKE '%141704%');

# increase relic drop rates
UPDATE ch_live_unitydatadb.loot_table_items SET weight = 100 WHERE (
  loot_table_id = 2649 OR
  loot_table_id = 2650 OR
  loot_table_id = 2651 OR
  loot_table_id = 2652 OR
  loot_table_id = 2653) AND
  weight < 50
```

Increase the base concentration regeneration to make it adaptive to the user's level. In the server's `CombatEntity.cs->Update()`:
```
# replace (Line ~1000)
CurrentConcentrationFishing += ConcentrationRegenPerTick + HwBaseConcentrationRegen;
# with 
CurrentConcentrationFishing += ConcentrationRegenPerTick + HwBaseConcentrationRegen + (int) (LevelFishing / 2);
```
