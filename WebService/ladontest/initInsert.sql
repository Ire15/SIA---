Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1', 'Activos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2', 'Pasivos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('3', 'Patrimonio', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('4', 'Ingresos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('5', 'Costos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6', 'Gastos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('7', 'Otros ingresos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('8', 'Otros gastos', '', 1, 0, 0);
Insert into `TipoMoneda` (nombre) values ('Local');
Insert into `TipoMoneda` (nombre) values ('Sistema');
Insert into `TipoMoneda` (nombre) values ('Extranjera');
Insert into `Estado` (nombre) values ('Abierto');
Insert into `Estado` (nombre) values ('Cerrado');
Insert into `Estado` (nombre) values ('Abierto excepto ventas');
Insert into `TipoAsiento` (nombre) values ('AS');
-- Inserts del profe --
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1', 'Activos Circulantes', '', 1, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-01', 'Efectivo y Bancos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-01-01', 'Caja Chica', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-01-02', 'Banco Nacional Dolares', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-01-03', 'Banco Nacional Colones', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-01-04', 'Banco de CR Colones', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-02', 'Cuentas por cobrar', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-02-01', 'Cuentas por cobrar locales', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-02-02', 'Cuentas por cobrar internacionales', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-03', 'Inventarios', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-03-01', 'Inventario General', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-03-02', 'Inventario Danado', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-1-03-03', 'Inventario Consignacion', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-2', 'Activos Fijos', '', 1, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-2-01', 'Terrenos, equipo, maquinaria', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-2-01-01', 'Equipo maquinaria', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('1-2-01-02', 'Depreciacion acumulada', '', 0, 0, 0);


Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-1', 'Pasivos a corto plazo', '', 1, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-1-01', 'Cuentas por pagar', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-1-01-01', 'Cuentas por pagar nacionales', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-1-01-02', 'Cuentas por pagar extranjero', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-2', 'Pasivos largo plazo', '', 1, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-2-01', 'Prestamos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('2-2-01-01', 'Hipoteca', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('3-1', 'Capital y Utilidades', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('3-1-01', 'Capital social', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('3-1-02', 'Utilidades retenidas', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('3-1-03', 'Perdidas y ganancias', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('4-1', 'Ventas', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('4-1-01', 'Ventas', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('4-1-02', 'Descuentos sobre Ventas', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('4-1-03', 'Devoluciones sobre Ventas', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('4-1-04', 'Ingreso por Consultoria', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('5-1', 'Costos de Ventas', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('5-1-01', 'Costo de Ventas', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-1', 'Gastos de Ventas', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-1-01', 'Bonificaciones', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-2', 'Gastos Administrativos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-2-01', 'Salarios', '', 0, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-2-02', 'Servicios Varios', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-3', 'Gastos de Operacion', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('6-3-01', 'Perdidas por inventario danado', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('7-1', 'Otros Ingresos', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('7-1-01', 'Ingresos Financieros', '', 0, 0, 0);

Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('8-1', 'Otros Gastos ', '', 1, 0, 0);
Insert into `Cuenta` (codigo, nombre, nombreExtranjero, titulo, saldoSistema, saldoLocal) values ('8-1-01', 'Gastos Financieros', '', 0, 0, 0);

