# Guarantee an Arcane Runes drop from Unox

* What: Ensures that Unox drops a Lexicon of the Arcane Runes.
* Why: Runes were originally designed to be a guaranteed drop from Proteus, however the bosses were never rebalanced after that change.
* Notes: None.
* Changes:
```
# add the only-Runes loot set to Unox (so Unox drops four items)
INSERT INTO ch_live_unitydatadb.mob_loot_sets (mob_template_id, loot_set_id, num_drops) VALUES (103025, 100365, 1)
```
