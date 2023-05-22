create database to_do_crud;
use to_do_crud;

create table tarefas(
id int primary key auto_increment,
task varchar(50)not null,
to_do bool not null,
doing bool not null,
done bool not null);


desc tarefas;
drop table tarefas;

select *from tarefas;

delete from tarefas where task=" ";