-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Requirements:
-- 
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction
-- Context: Write code in SQL is a nice level up!
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
    DECLARE total_projects INT DEFAULT 0;
    DECLARE current_project INT DEFAULT 0;

    SELECT COUNT(*) INTO total_projects FROM `projects` WHERE `name` = project_name;
    IF total_projects = 0 THEN
        INSERT INTO `projects`(`name`) VALUES (project_name);
    END IF;
    SELECT `id` INTO current_project FROM `projects` WHERE `name` = project_name;
    INSERT INTO `corrections` (`user_id`, current_project, `score`) VALUES (user_id, current_project, score);
END //
DELIMITER ;
