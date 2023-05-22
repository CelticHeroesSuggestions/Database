# Regenleif

* What: NPC for rares that are unattainable or infeasible (e.g., Bloodlust Helm, Golden Camouflage Charm, Kites, plat items). To our understanding, conversations use an XML format, to make it easy for DECA Games we have tried to replicate that.
* Why: These items do not make a significant impact on the endgame, but could help newer players.
* Table: various.
* Notes: I named the NPC Regenleif just out of convenience, but any Celtic name would fit. I placed the NPC in Lir's Reach, by the Tavern.
* Changes:

Add a new Dialogue (patchserver): `cv_leif_regenleif.xml`
```
<xml>
<line>
<lineTag>OPEN</lineTag>
<lineText>Hello there, [name]!  I am Regenleif, High Priest in the Order of Taranis.  I hail as a missionary to spread the sacred word and gifts from Taranis himself!  Behold my wares and heed these words: a great and powerful transformation is coming to Dal Riata, be ready!\n\nWould you like to see what I have to offer?
</lineText>
<choice>
<choiceOptions>[S]</choiceOptions>
<choiceText>Let's shop!</choiceText>
<choiceAction>SHOP 100001</choiceAction>
<choiceGoto>AFTER</choiceGoto>
</choice>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>No, thank you.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>AFTER</lineTag>
<lineText>It has been a pleasure meeting with you, [name].  Please visit again any time, all proceeds sponsor our missionary work.</lineText>
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
INSERT INTO ch_live_unitydatadb.mob_templates (mob_template_id, mob_name, aggro_range, follow_range, faction_id, opinion_base, level, hitpoints, loot_table, min_coins, max_coins, kills_per_level, conversation_id, attack, defence, attack_speed, energy, skill_list, radius, armour_value, model_scale, damage_list, resistance_list, mob_power, max_attack_range, mob_race, missile_speed, report_back_time, ai_template_id, xp, num_drops, perm_status_effects, blocks_attacks, avoidance_ratings, spot_hidden, immunity_list, damage_reductions_list, no_ability_test, mob_type)
VALUES (200001, 'Regenleif', 0, 0, 1, 51, 0, 100, NULL, 0, 0, NULL, 1001, 0, 0, 0, 0, NULL, .3, 5, 1, NULL, NULL, 0, 1, 20, 0, 0, 0, 0, 1, NULL, 0, NULL, 0, NULL, '7,1.00', 0, 0);

INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (100001, 2, 20, 233.65, 5, -245.33, 'stamd', '200001,1', 1, 160, 90, 0, 0, 0);
```

Add a new Shop (server)
```
# create the shop and attach to the Regenleif NPC
INSERT INTO ch_live_unitydatadb.shop (zone_id, shop_id, shop_name, npc_id, loot_table_id, loot_table_quantity, class_id, faction_id, faction_level)
VALUES (2, 100001, 'Regenleif Rares', 200001, -1, 0, 0, 0, 0);

# add the items to the shop
# golden camo
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 17657, -1, 0);
# golden shrink
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 17656, -1, 1);
# golden growth
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 17655, -1, 2);
# bloodlust
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 17000, -1, 3);
# golden axe of carnage
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 15018, -1, 4);
# eternal flight of vitality (+15% hp)
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 57248, -1, 5);
# eternal flight of replenishment (health regen)
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 57238, -1, 6);
# eternal flight of focus (+15% en)
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 57253, -1, 7);
# eternal flight of rejuvination (energy regen)
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 57243, -1, 8);
# eternal flight of guarding (armor)
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 57258, -1, 9);
# platinum lockbox
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 34784, -1, 10);
# Dragonfire Fists
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 51681, -1, 11);
# Archfyre Fists
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 54926, -1, 12);
# Everlasting Fireworks
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100001, 2, 53644, -1, 13);

# Set the Everlasting Fireworks cooldown to 0
INSERT INTO ch_live_unitydatadb.item_cooldowns (item_id, cooldown)
VALUES (53644, 0);

# update the Flight of Focus buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000 WHERE item_id = 57253;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 20000 WHERE item_id = 57253;

# update the Flight of Rejuvination buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000 WHERE item_id = 57243;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 20000 WHERE item_id = 57243;

# update the Flight of Replenishment buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000 WHERE item_id = 57238;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 20000 WHERE item_id = 57238;

# update the Flight of Vitality buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000 WHERE item_id = 57248;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 20000 WHERE item_id = 57248;

# update the Flight of Guarding buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000 WHERE item_id = 57258;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 20000 WHERE item_id = 57258;

# update the Platinum Lockbox buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 1000 WHERE item_id = 34784;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 2000 WHERE item_id = 34784;

# update the Dragonfire Fists buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 25000 WHERE item_id = 51681;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 50000 WHERE item_id = 51681;

# update the Archfyre Fists buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 25000 WHERE item_id = 54926;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 50000 WHERE item_id = 54926;

# update the Everlasting Fireworks buy and sell prices (so it can be in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000 WHERE item_id = 53644;
UPDATE ch_live_unitydatadb.item_templates SET sell_price = 20000 WHERE item_id = 53644;

# add the buy/sell price multipliers for item types
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 0, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 1, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 2, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 3, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 4, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 5, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 6, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 7, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 8, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 9, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 10, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 11, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 12, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 13, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 14, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 15, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 16, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 17, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 18, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 19, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 20, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 21, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 22, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 23, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 24, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 25, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 26, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 27, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 28, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 29, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 30, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 31, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 32, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 33, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 34, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 35, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 36, .5, 1);
INSERT INTO ch_live_unitydatadb.shop_subtype_prices (zone_id, shop_id, sub_type_id, buy_price_multiplier, sell_price_multiplier)
VALUES (2, 100001, 61, .5, 1);

```
