-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed

DELIMTER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email attribute is being updated
    IF NEW.email != OLD.email THEN
	SET NEW.valid_email = 0;
    END IF;
END;

$$

DELIMITER ;
