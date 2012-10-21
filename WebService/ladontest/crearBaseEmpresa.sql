SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `SIA_DB` ;
CREATE SCHEMA IF NOT EXISTS `SIA_DB` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;
USE `SIA_DB` ;

-- -----------------------------------------------------
-- Table `SIA_DB`.`Pais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SIA_DB`.`Pais` ;

CREATE  TABLE IF NOT EXISTS `SIA_DB`.`Pais` (
  `idPais` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(30) NOT NULL ,
  PRIMARY KEY (`idPais`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIA_DB`.`Empresa`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SIA_DB`.`Empresa` ;

CREATE  TABLE IF NOT EXISTS `SIA_DB`.`Empresa` (
  `idEmpresa` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  `cedula_juridica` VARCHAR(30) NOT NULL ,
  `logotipo` VARCHAR(100) NOT NULL ,
  `idPais` INT NOT NULL ,
  PRIMARY KEY (`idEmpresa`) ,
  INDEX `fk_Empresa_Pais_idx` (`idPais` ASC) ,
  CONSTRAINT `fk_Empresa_Pais`
    FOREIGN KEY (`idPais` )
    REFERENCES `SIA_DB`.`Pais` (`idPais` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIA_DB`.`TipoContacto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SIA_DB`.`TipoContacto` ;

CREATE  TABLE IF NOT EXISTS `SIA_DB`.`TipoContacto` (
  `idTipoContacto` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idTipoContacto`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIA_DB`.`Contacto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SIA_DB`.`Contacto` ;

CREATE  TABLE IF NOT EXISTS `SIA_DB`.`Contacto` (
  `idContacto` INT NOT NULL AUTO_INCREMENT ,
  `valor` VARCHAR(45) NOT NULL ,
  `idEmpresa` INT NOT NULL ,
  `idTipoContacto` INT NOT NULL ,
  PRIMARY KEY (`idContacto`) ,
  INDEX `fk_Contacto_Empresa1_idx` (`idEmpresa` ASC) ,
  INDEX `fk_Contacto_TipoContacto1_idx` (`idTipoContacto` ASC) ,
  CONSTRAINT `fk_Contacto_Empresa1`
    FOREIGN KEY (`idEmpresa` )
    REFERENCES `SIA_DB`.`Empresa` (`idEmpresa` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Contacto_TipoContacto1`
    FOREIGN KEY (`idTipoContacto` )
    REFERENCES `SIA_DB`.`TipoContacto` (`idTipoContacto` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIA_DB`.`TipoUsuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SIA_DB`.`TipoUsuario` ;

CREATE  TABLE IF NOT EXISTS `SIA_DB`.`TipoUsuario` (
  `idTipoUsuario` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idTipoUsuario`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIA_DB`.`Usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SIA_DB`.`Usuario` ;

CREATE  TABLE IF NOT EXISTS `SIA_DB`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  `pass` VARCHAR(32) NOT NULL ,
  `idEmpresa` INT NOT NULL ,
  `idTipoUsuario` INT NOT NULL ,
  PRIMARY KEY (`idUsuario`) ,
  INDEX `fk_Usuario_Empresa1_idx` (`idEmpresa` ASC) ,
  INDEX `fk_Usuario_TipoUsuario1_idx` (`idTipoUsuario` ASC) ,
  CONSTRAINT `fk_Usuario_Empresa1`
    FOREIGN KEY (`idEmpresa` )
    REFERENCES `SIA_DB`.`Empresa` (`idEmpresa` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_TipoUsuario1`
    FOREIGN KEY (`idTipoUsuario` )
    REFERENCES `SIA_DB`.`TipoUsuario` (`idTipoUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

insert into TipoContacto(nombre) values('Fax');
insert into TipoContacto(nombre) values('Telefono');
insert into TipoUsuario(nombre) values('Administrador');
