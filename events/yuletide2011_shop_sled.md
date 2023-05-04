# Yuletide 2011: Sled Mounts

* What: Spawn points for the Yuletide 2011 event shop NPC.
* Why: This is a legacy event shop that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points``.
* Notes: I placed the NPC in Farcrag near the fountain.
* Changes:
```
# Bob Slayer
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11503, 93, 10, 10.87, 0, -10.93, "stand", "145,1", 1, 290, 50, 0, 0, 0);

# Add a new shop
INSERT INTO ch_live_unitydatadb.shop (zone_id, shop_id, shop_name, npc_id, loot_table_id, loot_table_quantity, class_id, faction_id, faction_level)
VALUES (93, 100002, "Sled Shop", 145, -1, 0, 0, 0, 0);

# Add sleds to the shop
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17650, -1, 1);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17651, -1, 2);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17652, -1, 3);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17653, -1, 4);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17654, -1, 5);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17660, -1, 6);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (100002, 93, 17661, -1, 7);
```

Edit Bob Slayer's dialogue (`cv_sledge_trader.xml`)
```
<!-- Sledge Merchant -->

<xml>

<line>
<lineTag>OPEN</lineTag>
<lineText>I spend all the summer months creating these powerful enchanted sleds, then in Winter I bring them to Farcrag Castle for heroes like you, [class]. Would you like to take a look at my selection?</lineText>
<choice>
<choiceOptions>[S]</choiceOptions>
<choiceText>Yes please.</choiceText>
<choiceAction>SHOP 100002</choiceAction>
<choiceGoto>AFTER</choiceGoto>
</choice>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>No thank you.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>AFTER</lineTag>
<lineText>I'm only here for a brief period over Yuletide before I head back to my workshop. If you or any of your friends are after a sled, don't wait around before making a purchase! Oh, and don't forget that sleds are weapons that use the 'Novelty' ability. You can learn that ability from Fuggles the Jester right here in Farcrag Castle. Have a Merry Yuletide!</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

</xml>
```
