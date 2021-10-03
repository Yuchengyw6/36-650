-- q5
ALTER TABLE player_bios
ADD COLUMN position TEXT;
UPDATE player_bios 
SET position = a.position
from new_table as a
WHERE a.player = player_bios.id;

SELECT firstname, lastname, position FROM player_bios LIMIT 5;