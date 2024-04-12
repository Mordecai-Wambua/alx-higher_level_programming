-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT d.name, SUM(b.rate) AS `rating`
FROM tv_genres AS d
INNER JOIN tv_show_genres AS c
ON c.genre_id = d.id
INNER JOIN tv_show_ratings AS b
ON b.show_id = c.show_id
GROUP BY d.name
ORDER BY `rating` DESC;
