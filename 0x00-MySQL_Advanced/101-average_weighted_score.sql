-- 13. Average weighted score for all!
-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers 
-- that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE `users` ADD total_weighted_score INT NOT NULL, ADD total_weight INT NOT NULL;

    SELECT SUM(corrections.score * projects.weight) INTO users.total_weighted_score
        FROM corrections LEFT JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id;

    SELECT SUM(projects.weight) INTO users.total_weight
        FROM corrections LEFT JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id;

    UPDATE `users`
        SET `average_score` = IF(`total_weight` = 0, 0, `total_weighted_score` / `total_weight`);
    ALTER TABLE users DROP COLUMN total_weighted_score, DROP COLUMN total_weight;
END //
DELIMITER ;
