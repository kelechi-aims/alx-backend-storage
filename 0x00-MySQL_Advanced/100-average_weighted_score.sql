-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN 
	DECLARE total_weighted_score FLOAT;
	DECLARE total_weight INT;

	SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
	INTO total_weighted_score, total_weight
	FROM corrections
	JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	IF total_weight > 0 THEN
		UPDATE users
		SET users.average_score = total_weighted_score / total_weight
		WHERE users.ud = user_id;
	ELSE
		UPDATE users
		SET users. average_score = 0
		WHERE users.ud = user_id;
	END IF;
END $$

DELIMITER ;
