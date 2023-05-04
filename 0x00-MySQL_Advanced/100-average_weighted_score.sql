-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE weighted_average FLOAT DEFAULT 0;

    SELECT AVG(`corrections`.`score` * `projects`.`weight`)
        INTO weighted_average
        FROM `corrections` LEFT JOIN `projects`
            ON `corrections`.`project_id` = `projects`.`id` WHERE `corrections`.`user_id` = user_id;

    UPDATE `users`
            SET `users`.`average_score` = IFNULL(weighted_average, 0)
            WHERE `users`.`id` = user_id;
END //
DELIMITER ;
