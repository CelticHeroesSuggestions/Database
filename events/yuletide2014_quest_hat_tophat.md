# Yuletide 2014: Event Hat Quest (top hats)

* What: Spawn point for the Yuletide 2014 event quest.
* Why: This shop was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC at Farcrag's skill trainers, to give more content there.
* Changes:
```
# Kennis of the Snow (hat quest NPC shop)
# The mob template was deleted by OTM for whatever reason, so make it again

# on the server:

# Create the mob template
INSERT INTO ch_live_unitydatadb.mob_templates (mob_template_id, mob_name, aggro_range, follow_range, faction_id, opinion_base, level, hitpoints, loot_table, min_coins, max_coins, kills_per_level, conversation_id, attack, defence, attack_speed, energy, skill_list, radius, armour_value, model_scale, damage_list, resistance_list, mob_power, max_attack_range, mob_race, missile_speed, report_back_time, ai_template_id, xp, num_drops, perm_status_effects, blocks_attacks, avoidance_ratings, spot_hidden, immunity_list, damage_reductions_list, no_ability_test, mob_type)
VALUES (101131, 'Kennis of the Snow', 0, 25, 0, 51, 0, 64, NULL, 0, 2, NULL, 409, -5, 0, 2730, 32, NULL, 0.3, 0, 1, NULL, NULL, 0, 1, 18, 0, 0, 0, 80, 1, NULL, 0, NULL, 0, NULL, '7,1.00', 0, 0);

# Insert the spawn point
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14501, 93, 50, 82.28, 0, -23.4, "stand", "101131,1", 1, 190, 12, 0, 0, 0);

# weirdly, this quest was overwritted by the next year's event quest (Yuletide 2014 - Cranfir Crackers for Eagle Crests). A new quest is required, however that is for another day.

# as an interim fix, add the top hats to the wing shop
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53396, -1, 10);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53397, -1, 11);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53323, -1, 12);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53328, -1, 13);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53327, -1, 14);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53326, -1, 15);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53325, -1, 16);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53330, -1, 17);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53324, -1, 18);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53329, -1, 19);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53322, -1, 20);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12005, 93, 53321, -1, 21);

# set the buy and sell price for the top hats
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id >= 53301 AND item_id <= 53330;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 53397;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 53396;

# To add this quest yourself (if you make this, please make a pull request!):
# todo: create the quest
# todo: create the quest stages
# todo: create the quest reward loot set
# todo: create the quest reward

```

In `mob_data.txt` (patchserver), add:
```
101131,101048,0.3,Kennis of the Snow,2730,0,1,-1,18,0,1,1.8,0,0,1
```

Update the `text.db` file by patching the following:
```
# create the quest
# create the quest stages
```

Update the conversation `cv_winter2014_hat_quest.xml` to change the quest IDs to the new quest
