CREATE TABLE productos (
	id integer PRIMARY KEY AUTOINCREMENT,
	nombre varchar,
	description text,
	precio float,
	cantidad integer
);

CREATE TABLE usuarios (
	id integer PRIMARY KEY AUTOINCREMENT,
	nombre varchar,
	lastname varchar,
	email varchar,
	password varchar,
	telephone varchar
);

CREATE TABLE pedidos (
	id integer PRIMARY KEY AUTOINCREMENT,
	user_id integer,
	product_id integer,
	cantidad integer
);




