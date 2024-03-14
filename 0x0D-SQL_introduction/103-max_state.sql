-- displays the max temperature of each state (ordered by State name).
SELECT STATE, MAX(value) AS max_temp FROM temperatures GROUP BY STATE ORDER BY state ASC LIMIT 3;
