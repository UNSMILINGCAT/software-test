
create table a (
       st    number,
       hname varchar2(10),
       hpercent number
);


insert into a values (1,'bs',0.4);
insert into a values (1,'dl',1.28);
insert into a values (1,'ht',1.74);
insert into a values (2,'bd',37.94);
insert into a values (2,'zs',1.06);
insert into a values (2,'zs',0.97);
commit;
insert into a values(3,'db',1.74);
commit;

       
1.select hname from 
(select t.*,row_number() over(partition by st order by hpercent desc) rn from a t) where rn=1;



2.select hname from 
(select t.*,row_number() over(partition by st order by hpercent desc) rn from a t) where rn=2;

/*
 select * from 
(select e.* ,dense_rank() over (partition by st order by hpercent desc) rn from a e )  where rn=2;
*/    --另外一种方法











