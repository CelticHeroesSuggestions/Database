# Regenleif

* What: NPC for rares that are unattainable or infeasible (e.g., Bloodlust Helm, Golden Camouflauge Charm, Kites, plat items). To our understanding, conversations use an XML format, to make it easy for DECA Games we have tried to replicate that.
* Why: These items do not make a significant impact on the endgame, but could help newer players.
* Table: `ch_live_unitydatadb.spawn_points`.
* Notes: I named the NPC Regenleif just out of convenience, but any Celtic name would fit. I placed the NPC in Lir's Reach, by the Tavern.
* Changes:

Add a new Dialogue (patchserver): `cv_leif_regenleif.xml`
```
<xml>
<line>
<lineTag>OPEN</lineTag>
<lineText>Hello there! I am Regenleif, High Priest in the Order of Taranis. I hail as a missionary to spread the sacred word and gifts from Taranis himself! Behold my wares and heed these words: a great and powerful transformation is coming to Dal Riata, be ready!</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>
</xml>
```

Add a new Conversation (patchserver): `conversation_lookup.txt`
```
...
conv 1001 cv_leif_regenleif
END_FILE
```

Add a new Mob (patchserver): `mob_data.txt`
```
...
200001,173,0.3,Regenleif,0,0,1,-1,20,0,1,1.9,0,0,1
(end of file)
```

Add a new Mob (server):
```
INSERT INTO ch_live_unitydatadb.mob_templates (mob_template_id, mob_name, aggro_range, follow_range, faction_id, opinion_base, level, hitpoints, loot_table, min_coins, max_coins, kills_per_level, conversation_id, attack, defence, attack_speed, energy, skill_list, radius, armour_value, model_scale, damage_list, resistance_list, mob_power, max_attack_range, mob_race, missile_speed, report_back_time, ai_template_id, xp, num_drops, perm_status_effects, blocks_attacks, avoidance_ratings, spot_hidden, immunity_list, damage_reduction_list, no_ability_test, mob_type
200001, Regenleif, 0, 0, 1, 51, 0, 100, , 0, 0, , 1001, 0, 0, 0, 0, , .3, 5, 1, , , 0, 1, 20, 0, 0, 0, 0, 1, 0, , 0, 0, 7,1.00, 0, 0

INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (100001, 2, 20, 233.65, 5, -245.33, 'stamd', '200001,1', 1, 160, 90, 0, 0, 0);
```


