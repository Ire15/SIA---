DROP PROCEDURE IF EXISTS `crearTipoContacto`;
create procedure crearTipoContacto(IN pNombre varchar(45))
begin
declare tipoContactoEncontrado int;
select idTipoContacto from TipoContacto where nombre = pNombre into tipoContactoEncontrado;
if(tipoContactoEncontrado is null) then
begin
insert into TipoContacto (nombre) values (pNombre); 
end;
end if;
end !

DROP PROCEDURE IF EXISTS `crearContacto`;
create procedure crearContacto(pValor varchar(30), pNombreTipo varchar(45), pNombreEmpresa varchar(45))
begin
Declare idEmpresaEncontrado int;
Declare idTipoContactoEncontrado int;
Select idTipoContacto from TipoContacto where nombre = pNombreTipo into idTipoContactoEncontrado;
if(idTipoContactoEncontrado is null)  then
begin
call crearTipoContacto(pNombreTipo);
select max(idTipoContacto) into idTipoContactoEncontrado;
end;
end if;
if(idTipoEmpresaEncontrado is null)then
begin
set @resultado = -1;
end;
end if;
set @resultado = 0;
if(@resultado = 0) then
begin
Select idEmpresa from Empresa where nombre= pNombreEmpresa into idEmpresaEncontrado ;
Insert into Contacto (valor, idTipoContacto, idEmpresa) values (pValor, idTipoContactoEncontrado, idEmpresaEncontrado);
end;
end if;
end !

DROP PROCEDURE IF EXISTS `crearTipoUsuario`;
create procedure crearTipoUsuario(pNombre varchar(45))
begin
declare TipoUsuarioEncontrado int;
select idTipoUsuario from TipoUsuario where nombre = pNombre into TipoUsuarioEncontrado;
if(TipoUsuarioEncontrado is null) then
begin
insert into TipoUsuario (nombre) values (pNombre); 
end;
end if;
end !

DROP PROCEDURE IF EXISTS `crearUsuario`;
create procedure crearUsuario(pUsuario varchar(45), pContrasena varchar(32), pTipoUsuario varchar(45), pEmpresa varchar(45))
begin
declare idTipoUsuarioEncontrado, idEmpresaEncontrada int;
Select idTipoUsuario from TipoUsuario where nombre = pTipoUsuario into idTipoUsuarioEncontrado;
Select idEmpresa from Empresa where nombre = pEmpresa into idEmpresaEncontrada;
insert into Usuario(nombre, pass, idTipoUsuario, idEmpresa) values (pUsuario, pContrasena,idTipoUsuarioEncontrado, idEmpresaEncontrada);
end! 

DROP PROCEDURE IF EXISTS `crearPais`;
create procedure crearPais(pNombre varchar(30))
begin
declare PaisEncontrado int;
select idPais from Pais where nombre = pNombre into PaisEncontrado;
if(PaisEncontrado is null) then
begin
insert into Pais (nombre) values (pNombre); 
end;
end if;
end !

DROP PROCEDURE IF EXISTS `crearEmpresa`;
create procedure crearEmpresa(pNombre varchar(45), pCedulaJuridica varchar(30), pLogotipo varchar(100), pPais varchar(30))
begin
declare idPaisEncontrado int;
Select idPais from Pais where nombre = pPais into idPaisEncontrado;
if(idPaisEncontrado is null) then
begin
call crearPais(pPais);
Select idPais from Pais where nombre = pPais into idPaisEncontrado;
end;
end if;
insert into Empresa(nombre, cedula_juridica, logotipo, idPais) values (pNombre, pCedulaJuridica, pLogotipo, idPaisEncontrado);
end! 

DROP PROCEDURE IF EXISTS `pedirUsuario`;
create procedure pedirUsuario(pNombreUsuario varchar(20))
begin
select nombre, pass, idTipoUsuario from Usuario where nombre = pNombreUsuario;
end!

DROP PROCEDURE IF EXISTS `pedirEmpresa`;
create procedure pedirEmpresa(pNombreEmpresa varchar(45))
begin
select Empresa.nombre, Empresa.cedula_juridica, Empresa.logotipo, Pais.nombre from 
Empresa inner join Pais on (Empresa.Pais_idPais=Pais.idPais) where Empresa.nombre=pNombreEmpresa;
end!

DROP PROCEDURE IF EXISTS `pedirContactos`;
create procedure pedirContactos(pNombreEmpresa varchar(45))
begin
select Contacto.valor, TipoContacto.nombre from Empresa 
inner join Contacto on (Empresa.idEmpresa=Contacto.Empresa_id) 
inner join TipoContacto on (Contacto.TipoContacto_idTipoContacto=TipoContacto.idTipoContacto);
end!

DROP PROCEDURE IF EXISTS `pedirEmpresas`;
create procedure pedirEmpresas()
begin
select Empresa.nombre from Empresa;
end!

