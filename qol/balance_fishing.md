# Balancing Fishing

* What: Balances fishing for solo play.
* Why: Drop rates of certain fishing items and spawns is too low.
* Notes: N/A
* Changes:
```
# remove Glacial Waters: the spawns are normal spawns followed by the various Glacial spawns, so can safely only include the spawns left of the first '141690' 
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = left(monster_list, locate('141690', monster_list) - 1) WHERE monster_list LIKE '%141690%';

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
