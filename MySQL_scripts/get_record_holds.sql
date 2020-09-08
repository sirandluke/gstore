SELECT 
	CONCAT(recordHolds.first_name,' ', recordHolds.last_name) AS 'Name',
    CONCAT(records.album, ' by ', records.artist) AS 'Record Reserved',
    recordHolds.hold_date AS 'Date Reserved'
FROM records
INNER JOIN recordHolds
ON recordHolds.rec_id = records.recId
ORDER BY recordHolds.hold_date;
