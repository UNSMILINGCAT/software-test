# 存储过程
/*
  解释：
    将多个SQL语句封装到一起，这样的一个SQL脚本就是存储过程，
    存储过程类似于函数
  语法：
  create procedure 存储过程名称(参数)
  begin
    SQL语句
  end
  
  delimiter 声明，存储过程结束符号的声明 
  存储过程默认是以;结束
*/
-- 案例1：创建一个简单的存储过程
DROP PROCEDURE myp1;  #删除存储过程

DELIMITER $  # 设置存储过程的结束符号
CREATE PROCEDURE myp1()
BEGIN 
    INSERT INTO mystu VALUES(NULL,'myprocedure',99);
    SELECT * FROM mystu;
END$

-- 调用存储过程
CALL myp1();

-- 案例2：创建带有参数的存储过程
DROP PROCEDURE myp2;

DELIMITER $  # 设置存储过程的结束符号
CREATE PROCEDURE myp2(cj INT,NAME VARCHAR(30))
BEGIN 
    INSERT INTO mystu VALUES(NULL,NAME,cj);
    SELECT * FROM mystu;
END$

CALL myp2(78,'lisi');

-- 案例3：加入判断条件的存储过程
DELIMITER $
# 当flag为1的时候，统计工资10000以上员工的个数
# 当flag为其它值得时候，统计工资小于或等于10000的员工个数
DELIMITER $
CREATE PROCEDURE myp4(flag INT) 
BEGIN 
  IF flag=1 THEN
	SELECT CONCAT("工资大于10000的员工有 ",COUNT(*)," 个") FROM emp WHERE sal > 10000;
  ELSE
	SELECT CONCAT("工资小于等于10000的员工有 ",COUNT(*)," 个") FROM emp WHERE sal <= 10000;
  END IF;# if也需要使用end if结束
END$

CALL myp4(0);

/*
delimiter $
create procedure myp3(page int,pageSize int)
begin 
  declare sta int;
  set sta = (page-1)*pageSize;
  select * from emp limit sta,pageSize;
end$

call myp3(3,3);
*/

-- 案例4：在存储过程中加入循环
-- 计算1到N的和
DELIMITER $
CREATE PROCEDURE myp5(n INT)
BEGIN 
  DECLARE i INT;# 声明一个变量  用来迭代
  DECLARE he INT;# 声明一个变量，用来存储和
  SET i = 1;
  SET he = 0;
  WHILE i<=n DO
    SET he = he + i;
    SET i=i+1;
  END WHILE;
  SELECT he;#查询总和
END$

CALL myp5(10);


-- 索引
/*
  索引主要是提高检索效率（查询）
  底层原理：
   给数据进行分类，加上目录
*/
-- 创建索引
CREATE INDEX ename_index ON emp(ename(50));

ALTER TABLE emp ADD INDEX name_index(ename(50));

-- 删除索引
DROP INDEX ename_index ON emp;


-- 视图
/*
  视图就是将查询结果封装，但是是一个虚拟表
  语法：
  create view 视图名
  as 查询语句;
*/
CREATE OR REPLACE VIEW emp_dept_v
AS SELECT d.dname,d.loc  # 注释
FROM emp e
JOIN dept d
ON e.deptno=d.deptno;

-- 查询视图和查询表的语法一致
SELECT * FROM emp_dept_v;

-- 删除视图
DROP VIEW emp_dept_v;


-- 查看当前数据库使用的编码格式
SHOW VARIABLES LIKE 'char%';

