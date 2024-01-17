-- a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$
CREATE TRIGGER email_val BEFORE UPDATE ON `users`
FOR EACH ROW
	BEGIN
		IF NEW.email != OLD.email THEN
			SET NEW.valid_email = 0;
		END IF;
	END$$
DELIMITER ;
