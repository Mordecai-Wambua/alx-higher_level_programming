0x0E. SQL - More queries

Task 00:(0-privileges.sql)
lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

Task 01:(1-create_user.sql)
creates the MySQL server user user_0d_1
	user_0d_1 should have all privileges on your MySQL server
	The user_0d_1 password should be set to user_0d_1_pwd
	If the user user_0d_1 already exists, your script should not fail

Task 02:(2-create_read_user.sql)
creates the database hbtn_0d_2 and the user user_0d_2
	user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
	The user_0d_2 password should be set to user_0d_2_pwd

Task 03:(3-force_name.sql)
creates the table force_name on your MySQL server
 force_name description:
	id INT
	name VARCHAR(256) can’t be null

Task 04:(4-never_empty.sql)
creates the table id_not_null on your MySQL server.
id_not_null description:
	id INT with the default value 1
	name VARCHAR(256)

Task 05:(5-unique_id.sql)
creates the table unique_id on your MySQL server.
unique_id description:
	id INT with the default value 1 and must be unique
	name VARCHAR(256)

Task 06:(6-states.sql)
creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
states description:
	id INT unique, auto generated, can’t be null and is a primary key
	name VARCHAR(256) can’t be null

Task 07:(7-cities.sql)
creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
cities description:
	id INT unique, auto generated, can’t be null and is a primary key
	state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
	name VARCHAR(256) can’t be null

Task 08:(8-cities_of_california_subquery.sql)
lists all the cities of California that can be found in the database hbtn_0d_usa
	The states table contains only one record where name = California (but the id can be different, as per the example)
	Results must be sorted in ascending order by cities.id
	You are not allowed to use the JOIN keyword
	The database name will be passed as an argument of the mysql command

Task 09:(9-cities_by_state_join.sql)
lists all cities contained in the database hbtn_0d_usa
	Each record should display: cities.id - cities.name - states.name
	Results must be sorted in ascending order by cities.id
	You can use only one SELECT statement
	The database name will be passed as an argument of the mysql command

Task 10:(10-genre_id_by_show.sql)
Import the database dump from hbtn_0d_tvshows to your MySQL server: download

Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
