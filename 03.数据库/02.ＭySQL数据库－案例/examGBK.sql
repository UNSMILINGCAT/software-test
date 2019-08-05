DROP DATABASE exam;
CREATE DATABASE exam CHARSET=utf8;  

USE exam;

/*�������ű�*/
CREATE TABLE dept(
	deptno		INT 	PRIMARY KEY,
	dname		VARCHAR(50),
	loc 		VARCHAR(50)
);

/*������Ա��*/
CREATE TABLE emp(
	empno		INT 	PRIMARY KEY,
	ename		VARCHAR(50),
	job		VARCHAR(50),
	mgr		INT,
	hiredate	DATE,
	sal		DECIMAL(7,2),
	COMM 		DECIMAL(7,2),
	deptno		INT,
	CONSTRAINT fk_emp FOREIGN KEY(mgr) REFERENCES emp(empno)
);

/*�������ʵȼ���*/
CREATE TABLE salgrade(
	grade		INT 	PRIMARY KEY,
	losal		INT,
	hisal		INT
);

/*����ѧ����*/
CREATE TABLE stu(
	sid		INT 	PRIMARY KEY,
	sname		VARCHAR(50),
	age		INT,
	gander		VARCHAR(10),
	province	VARCHAR(50),
	tuition		INT
);







/*����dept������*/
INSERT INTO dept VALUES (10, '���в�', '����');
INSERT INTO dept VALUES (20, 'ѧ����', '�Ϻ�');
INSERT INTO dept VALUES (30, '���۲�', '����');
INSERT INTO dept VALUES (40, '����', '�人');

/*����emp������*/
INSERT INTO emp VALUES (1009, '����ţ', '���³�', NULL, '2001-11-17', 50000, NULL, 10);
INSERT INTO emp VALUES (1004, '����', '����', 1009, '2001-04-02', 29750, NULL, 20);
INSERT INTO emp VALUES (1006, '����', '����', 1009, '2001-05-01', 28500, NULL, 30);
INSERT INTO emp VALUES (1007, '�ŷ�', '����', 1009, '2001-09-01', 24500, NULL, 10);
INSERT INTO emp VALUES (1008, '�����', '����ʦ', 1004, '2007-04-19', 30000, NULL, 20);
INSERT INTO emp VALUES (1013, '��ͳ', '����ʦ', 1004, '2001-12-03', 30000, NULL, 20);
INSERT INTO emp VALUES (1002, '���˿', '����Ա', 1006, '2001-02-20', 16000, 3000, 30);
INSERT INTO emp VALUES (1003, '������', '����Ա', 1006, '2001-02-22', 12500, 5000, 30);
INSERT INTO emp VALUES (1005, 'лѷ', '����Ա', 1006, '2001-09-28', 12500, 14000, 30);
INSERT INTO emp VALUES (1010, 'ΤһЦ', '����Ա', 1006, '2001-09-08', 15000, 0, 30);
INSERT INTO emp VALUES (1012, '����', '��Ա', 1006, '2001-12-03', 9500, NULL, 30);
INSERT INTO emp VALUES (1014, '�Ƹ�', '��Ա', 1007, '2002-01-23', 13000, NULL, 10);
INSERT INTO emp VALUES (1011, '��̩', '��Ա', 1008, '2007-05-23', 11000, NULL, 20);


INSERT INTO emp VALUES (1001, '����', '��Ա', 1013, '2000-12-17', 8000, NULL, 20);


/*����salgrade������*/
INSERT INTO salgrade VALUES (1, 7000, 12000);
INSERT INTO salgrade VALUES (2, 12010, 14000);
INSERT INTO salgrade VALUES (3, 14010, 20000);
INSERT INTO salgrade VALUES (4, 20010, 30000);
INSERT INTO salgrade VALUES (5, 30010, 99990);

/*����stu������*/
INSERT INTO `stu` VALUES ('1', '����', '23', '��', '����', '1500');
INSERT INTO `stu` VALUES ('2', '����', '25', '��', '����', '2500');
INSERT INTO `stu` VALUES ('3', '��ǿ', '22', '��', '����', '3500');
INSERT INTO `stu` VALUES ('4', '������', '25', '��', '����', '1500');
INSERT INTO `stu` VALUES ('5', '������', '23', 'Ů', '����', '1000');
INSERT INTO `stu` VALUES ('6', '����', '22', 'Ů', 'ɽ��', '2500');
INSERT INTO `stu` VALUES ('7', '����', '21', 'Ů', '����', '1600');
INSERT INTO `stu` VALUES ('8', '����', '23', '��', '����', '3500');
INSERT INTO `stu` VALUES ('9', '����', '23', 'Ů', '����', '2500');
INSERT INTO `stu` VALUES ('10', '����', '18', '��', 'ɽ��', '3500');
INSERT INTO `stu` VALUES ('11', '����', '23', '��', '����', '4500');
INSERT INTO `stu` VALUES ('12', '����', '24', '��', '����', '1500');
INSERT INTO `stu` VALUES ('13', '����', '24', '��', '����', '2500');
INSERT INTO `stu` VALUES ('14', '����', '22', '��', '����', '3500');
INSERT INTO `stu` VALUES ('15', '��С��', '25', '��', '����', '1500');
INSERT INTO `stu` VALUES ('16', '��С��', '23', 'Ů', '����', '1000');
INSERT INTO `stu` VALUES ('17', '����', '22', 'Ů', 'ɽ��', '2500');
INSERT INTO `stu` VALUES ('18', '����', '21', 'Ů', '����', '1600');
INSERT INTO `stu` VALUES ('19', '����', '23', '��', '����', '3500');
INSERT INTO `stu` VALUES ('20', '����', '23', 'Ů', '����', '2500');
INSERT INTO `stu` VALUES ('21', '���', '18', '��', 'ɽ��', '3500');
INSERT INTO `stu` VALUES ('22', '����', '23', '��', '����', '4500');
INSERT INTO `stu` VALUES ('23', '�԰�', '23', '��', '����', '1500');
INSERT INTO `stu` VALUES ('24', '����', '25', '��', '����', '2500');
INSERT INTO `stu` VALUES ('25', '����', '22', '��', '����', '3500');
INSERT INTO `stu` VALUES ('26', '�𰲹�', '25', '��', '����', '1500');
INSERT INTO `stu` VALUES ('27', '�º���', '23', 'Ů', '����', '1000');
INSERT INTO `stu` VALUES ('28', '����', '22', 'Ů', 'ɽ��', '2500');
INSERT INTO `stu` VALUES ('29', '����', '21', 'Ů', '����', '1600');
INSERT INTO `stu` VALUES ('30', '���ι�', '23', '��', '����', '3500');
INSERT INTO `stu` VALUES ('31', '����', '23', 'Ů', '����', '2500');
INSERT INTO `stu` VALUES ('32', '��ǿ', '18', '��', 'ɽ��', '3500');
INSERT INTO `stu` VALUES ('33', '����', '23', '��', '����', '4500');
INSERT INTO `stu` VALUES ('34', '������', '23', '��', '����', '1500');
INSERT INTO `stu` VALUES ('35', '����', '25', '��', '����', '2500');
INSERT INTO `stu` VALUES ('36', '��ǿ', '22', '��', '����', '3500');
INSERT INTO `stu` VALUES ('37', '��Ϲ�', '25', '��', '����', '1500');
INSERT INTO `stu` VALUES ('38', '��С��', '23', 'Ů', '����', '1000');
INSERT INTO `stu` VALUES ('39', '����', '22', 'Ů', 'ɽ��', '2500');
INSERT INTO `stu` VALUES ('40', '�뺬', '21', 'Ů', '����', '1600');
INSERT INTO `stu` VALUES ('41', '�¶�', '23', '��', '����', '3500');
INSERT INTO `stu` VALUES ('42', '����', '23', 'Ů', '����', '2500');
INSERT INTO `stu` VALUES ('43', '����', '18', '��', 'ɽ��', '3500');
INSERT INTO `stu` VALUES ('44', '����', '23', '��', '����', '4500');
INSERT INTO `stu` VALUES ('45', '����', '23', '��', '����', '1500');
INSERT INTO `stu` VALUES ('46', '�Ź���', '25', '��', '����', '2500');
INSERT INTO `stu` VALUES ('47', '��Сǿ', '22', '��', '����', '3500');
INSERT INTO `stu` VALUES ('48', '�ض���', '25', '��', '����', '1500');
INSERT INTO `stu` VALUES ('49', '��С��', '23', 'Ů', '����', '1000');
INSERT INTO `stu` VALUES ('50', '����', '22', 'Ů', 'ɽ��', '2500');
INSERT INTO `stu` VALUES ('51', '����', '21', 'Ů', '����', '1600');
INSERT INTO `stu` VALUES ('52', 'ǮС��', '23', '��', '����', '3500');
INSERT INTO `stu` VALUES ('53', '����', '23', 'Ů', '����', '2500');
INSERT INTO `stu` VALUES ('54', '����', '18', '��', 'ɽ��', '3500');
INSERT INTO `stu` VALUES ('55', '����ǿ', '23', '��', '����', '4500');


/*
select * from emp;
select * from dept;
select * from salgrade;
*/