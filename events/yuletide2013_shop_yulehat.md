# Yuletide 2013: Yule Hats

* What: Adding the special offer yule hats to the shop.
* Why: These hats were cool and would make a nice reappearance to the game.
* Notes: I placed the hats into the Yuletide 2013 Luxury Shop
* Changes:
```
# Green Effect Hat
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12001, 93, 50661, -1, 1350);
# Blue Effect Hat
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12001, 93, 50660, -1, 1351);
# Red Effect Hat
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (12001, 93, 51121, -1, 1352);

# add a price to the hats (so they show up in the shop)
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 50658;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 50659;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 50660;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 50661;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 51121;
```
