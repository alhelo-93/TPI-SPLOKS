CREATE DEFINER=`root`@`localhost` TRIGGER `customers_AFTER_UPDATE` AFTER UPDATE ON `customers` FOR EACH ROW BEGIN
SET @Change = '';
IF OLD.firstname <> new.firstname THEN
SET @Change = CONCAT('Modification au ', OLD.firstname);
INSERT INTO logs(clientId,text) VALUES(old.id,@Change);
END IF;
IF OLD.lastname <> new.lastname THEN
SET @Change = CONCAT('Modification au ', OLD.lastname);
INSERT INTO logs(clientId,text) VALUES(old.id,@Change);
END IF;
IF OLD.address <> new.address THEN
SET @Change = CONCAT('Modification au ', OLD.address);
INSERT INTO logs(clientId,text) VALUES(old.id,@Change);
END IF;
IF OLD.email <> new.email THEN
SET @Change = CONCAT('Modification au ', OLD.email);
INSERT INTO logs(clientId,text) VALUES(old.id,@Change);
END IF;
IF OLD.mobile <> new.mobile THEN
SET @Change = CONCAT('Modification au ', OLD.mobile);
INSERT INTO logs(clientId,text) VALUES(old.id,@Change);
END IF;
END