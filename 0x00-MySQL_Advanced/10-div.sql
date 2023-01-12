-- Create function SafeDiv that divides (and returns) the first by the second number
-- or returns 0 if second number is equal to 0
-- function SafeDiv takes 2 arguments: a, INT, b, INT
-- returns a / b or 0 if b == 0

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER ;
