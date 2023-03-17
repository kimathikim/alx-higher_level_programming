-- script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter
SELECT t1.name
FROM tv_genres t1
    RIGHT JOIN tv_show_genres t2 ON t1.id = t2.genre_id
    WHERE t2.show_id = 8
ORDER BY name;
