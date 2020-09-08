SELECT 
	CONCAT(gameHolds.first_name,' ', gameHolds.last_name) AS 'Name',
    games.title AS 'Game Reserved',
    gameHolds.hold_date AS 'Date Reserved'
FROM games
INNER JOIN gameHolds
ON gameHolds.game_id = games.gameId
ORDER BY gameHolds.hold_date;
SELECT * FROM gameHolds;