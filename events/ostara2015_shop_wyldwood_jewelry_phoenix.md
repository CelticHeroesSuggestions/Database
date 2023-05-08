# Ostara 2015 Jewelry and Phoenixes

* What: Spawn points for the Ostara 2015 event shops.
* Why: These shops were very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPCs near Stonevale Farm to give more content there.
* Changes:
```
# Gayle the Hunter (jewelry trader)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15101, 3, 50, 90.32, 40, -67.50, "stand", "878,1", 1, 340, 12, 0, 0, 0);

# Move her shop to Stonevale
UPDATE ch_live_unitydatadb.shop SET zone_id = 3 WHERE shop_id = 1081;
UPDATE ch_live_unitydatadb.shop_stock SET zone_id = 3 WHERE shop_id = 1081;

# Raghnall the Hunter (phoenix mount trader) is reused for the Ostara 2016 shop, so spawn via that script instead 

# add the Phoenixes to the Ostara 2016 shop
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (15025, 2, 51554, -1, 20);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (15025, 2, 51555, -1, 21);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (15025, 2, 51556, -1, 22);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (15025, 2, 51557, -1, 23);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (15025, 2, 51558, -1, 24);
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (15025, 2, 51559, -1, 25);

# update the Phoenix staff buy prices
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 5000, sell_price = 10000 WHERE item_id = 51554;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 10000, sell_price = 20000 WHERE item_id = 51555;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 20000, sell_price = 40000 WHERE item_id = 51556;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 40000, sell_price = 80000 WHERE item_id = 51557;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 80000, sell_price = 160000 WHERE item_id = 51558;
UPDATE ch_live_unitydatadb.item_templates SET buy_price = 150000, sell_price = 300000 WHERE item_id = 51559;


```
