-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE weighted_average FLOAT DEFAULT 0;
    DECLARE project_weight FLOAT DEFAULT 0;

    SELECT SUM(projects.weight)
        INTO project_weight
        FROM corrections LEFT JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
    
    SELECT AVG(`corrections`.`score` * `projects`.`weight`)
        INTO weighted_average
        FROM `corrections` INNER JOIN `projects`
            ON `corrections`.`project_id` = `projects`.`id` WHERE `corrections`.`user_id` = user_id;
    IF project_weight <> 0 THEN
        UPDATE `users`
            SET `users`.`average_score` = IFNULL(weighted_average, 0)
            WHERE `users`.`id` = user_id;
    ELSE
        UPDATE users
        SET users.average_score = 0
        WHERE users.id = user_id;
    END IF;
END //
DELIMITER ;
