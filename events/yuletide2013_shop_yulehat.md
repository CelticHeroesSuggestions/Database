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
```
