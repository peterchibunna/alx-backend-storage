-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE average_score FLOAT DEFAULT 0;

    SELECT AVG(score)
        INTO average_score
        FROM `corrections`
        WHERE `corrections`.user_id = user_id;

    UPDATE users
        SET users.average_score = average_score
        WHERE users.id = user_id;
END //
DELIMITER ;
