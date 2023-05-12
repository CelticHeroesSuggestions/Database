# Rare Mob Spawn Rates

* What: Increase the spawn chance of certain rare mobs.
* Why: The content from those mobs is cool, but they are just too rare.
* Notes: None.
* Changes:
```
# Blademaster Dolal
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '70282,250;70289,250;70356,250;142015,148' WHERE spawn_point_id = 356;

# Apostate and Banished Mobs
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '102100,50;102101,50;102102,50;102874,50;142003,5' WHERE spawn_point_id = 3346;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '1021245,50;102125,50;102126,50;102127,50;142003,5' WHERE spawn_point_id = 3394;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '102124,50;102125,50;102126,50;142003,5' WHERE spawn_point_id = 3402;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '138175,75;138176,75;142002,5' WHERE spawn_point_id = 3462;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '138180,75;138181,75;142002,5' WHERE spawn_point_id = 3463;
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '138180,75;138181,75;142002,5' WHERE spawn_point_id = 3465;

# Hellflame Troll
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;141997,5' WHERE spawn_point_id = 2109;

# Wyrmheart Ironghast
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142011,5' WHERE spawn_point_id = 3548;

# Drowner of the Dark Moor
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142010,5' WHERE spawn_point_id = 776;

# Novamane
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142009,5' WHERE spawn_point_id = 811;

# Manifested Nightmare
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142008,5' WHERE spawn_point_id = 947;

# Weaponmaster Krish
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142004,5' WHERE spawn_point_id = 4794;

# Dragoncult Overlord
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142000,1' WHERE spawn_point_id = 1565;

# Dragoncult Grandmystic
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142001,1' WHERE spawn_point_id = 2258;

# Ainfean the Reaper
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;141998,1' WHERE spawn_point_id = 6663;

# Fionuir the Eternal
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;141999,1' WHERE spawn_point_id = 6408;

# The Dancing Corpse
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142013,1' WHERE spawn_point_id = 2780;

# The Singing Bones
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142014,1' WHERE spawn_point_id = 2792;

# Fionuir the Eternal
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;141999,1' WHERE spawn_point_id = 6408;

# Blade of Duhblainn
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142016,1' WHERE spawn_point_id = 973;

# Maneater Bear
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142017,1' WHERE spawn_point_id = 4665;

# Ancestral Bear
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142018,1' WHERE spawn_point_id = 420;

# Bronn the Mad Boar
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142019,1' WHERE spawn_point_id = 2753;

# Lone Tranquilsoul
UPDATE ch_live_unitydatadb.spawn_points SET monster_list = '-1,1000;142020,1' WHERE spawn_point_id = 3832;
```
