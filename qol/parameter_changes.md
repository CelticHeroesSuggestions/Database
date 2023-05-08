# Parameter Changes: 5x XP, 5x Gold, 10x Cooking Crit

* What: Globally increase several parameters.
* Why: Leveling is far too slow, and should be 1 elix/level at the most. This helps towards that goal. Additionally, it is challenging for new players to acquire gold.
* Notes: It would be nice to dynamically adapt this to player level, however, that is currently infeasible.
* Changes:
```
# increase the XP rate
UPDATE ch_live_unitydatadb.params SET param_value = 5.0 WHERE param_name = 'global exp rate';

# increase the gold rate
UPDATE ch_live_unitydatadb.params SET param_value = 5.0 WHERE param_name = 'global gold rate';

# increase the cooking success rate
UPDATE ch_live_unitydatadb.params SET param_value = 10.0 WHERE param_name = 'critical success rate for cooking';

# decrease the full heal logout time
UPDATE ch_live_unitydatadb.params SET param_value = 5 WHERE param_name = 'FULL_HEAL_LOGOUT_TIME';

# increase the critical XP multiplier
UPDATE ch_live_unitydatadb.params SET param_value = 5 WHERE param_name = 'xp crit multiplier';

# increase the critical gold multiplier
UPDATE ch_live_unitydatadb.params SET param_value = 5 WHERE param_name = 'gold crit multiplier';
```
