-- script that lists all genres from hbtn_0d_tvshows
SELECT name AS genre,
    count(name) AS number_of_shows
FROM tv_genres t1
    LEFT JOIN tv_show_genres t2 ON t1.id = t2.genre_id
GROUP BY(genre)
ORDER BY number_of_shows DESC;
