# 子查询 （难点）
/*
  子查询解释：
    查询里面嵌套查询，外面的查询称为主查询，
    里面嵌套的查询就是子查询
  语法：
  select 查询列表(子查询)
  from 表名(子查询)
  where 条件表达式（子查询）  -- 常用
  group by 分组列表
  having 分组后过滤（子查询） -- 常用
  exists （子查询）
  
  注意：
	①子查询一般会比主查询优先执行，并将结果给主查询使用
	②子查询如果是作为过滤条件，则一般会放在条件右边
	③子查询一般会使用()包起来
*/
-- 案例1：查询工资比刘备高的员工信息
SELECT *
FROM emp
WHERE sal > (SELECT sal 
FROM emp 
WHERE ename = '刘备');


/*
 子查询分类：
   根据子查询返回的结果进行分类：
    单行子查询：   返回一行一列数据的子查询称为单行子查询，
            一般结果单行操作符使用：
                >  <  >= <= =  <>
    多行子查询：   返回多行一列的子查询称为多行子查询
	    一般会结合多行操作符使用：
		in  any  all
*/
-- 案例2：查询工资比20号部门所有员工工资都高的员工信息
-- a.使用单行操作符实现
SELECT *
FROM emp
WHERE sal > (SELECT MAX(sal)
FROM emp 
WHERE deptno=20);

/*
  all 的使用，表示全部都
  >all 等同于>最大值
  <all 等同于<最小值
*/
SELECT *
FROM emp
WHERE sal > ALL (SELECT sal 
FROM emp WHERE deptno=20);

-- 案例3：查询员工工资大于10号部门任一员工的员工信息，不包含10号部门的员工
-- 其实就是查询工资大于10号部门最低工资的员工
SELECT *
FROM emp 
WHERE sal > (SELECT MIN(sal)
FROM emp
WHERE deptno=10)
AND deptno <>10;

/*
  any 的使用，表示任一，其中一个
  <any 等同于小于最大值
  >any 等同于大于最小值 
*/
SELECT *
FROM emp
WHERE sal > ANY(SELECT sal 
FROM emp WHERE deptno=10);

-- 案例4： 查询工作和工资与诸葛亮完全相同的员工信息分析
SELECT *
FROM emp 
WHERE (job,sal) IN (
  SELECT job,sal
  FROM emp 
  WHERE ename = '诸葛亮'
);


-- 案例5：在from后面使用子查询
SELECT t.*
FROM (SELECT * FROM emp) t
WHERE t.empno>1002;


-- 案例6：在select后面使用子查询
SELECT e.*,(SELECT d.dname FROM dept d WHERE d.deptno = e.deptno)
FROM emp e;






