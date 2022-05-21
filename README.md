一个解析nmap输出结果并将结果存储到数据的例子.


##### 创建数据库
```bash
mysql> create database fingers_db default character set utf8mb4 collate utf8mb4_unicode_ci;
```

##### 创建数据表
```bash
mysql> create table if not exists `osfingers`( 
    -> id int unsigned auto_increment primary key, 
    -> address varchar(100), 
    -> mac varchar(120), 
    -> name varchar(120), 
    -> accuracy varchar(120),
    -> type varchar(50), 
    -> vendor varchar(50), 
    -> osfamily varchar(50), 
    -> osgen varchar(50)
);

mysql> create table if not exists `ssfingers`(
    -> id int unsigned auto_increment primary key,
    -> port smallint,
    -> state varchar(30),
    -> reason varchar(30),
    -> name varchar(30),
    -> product varchar(50),
    -> version varchar(50),
    -> extrainfo varchar(80),
    -> conf varchar(30)
    -> );

```

##### 运行脚本
```bash
python3 cnmap.py 192.168.x.x
```

#### 查询结果
```bash
mysql> select * from osfingers;
+----+--------------+--------+--------------------------------------------------+----------+-----------------+--------+----------+-------+
| id | address      | mac    | name                                             | accuracy | type            | vendor | osfamily | osgen |
+----+--------------+--------+--------------------------------------------------+----------+-----------------+--------+----------+-------+
|  1 | 192.168.10.1 | Unknow | Linux 3.2                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
|  2 | 192.168.10.1 | Unknow | Linux 3.12 - 4.10                                | 96       | general purpose | Linux  | Linux    | 4.X   |
|  3 | 192.168.10.1 | Unknow | Linux 3.2.0                                      | 92       | general purpose | Linux  | Linux    | 3.X   |
|  4 | 192.168.10.1 | Unknow | Linux 3.10                                       | 93       | general purpose | Linux  | Linux    | 3.X   |
|  5 | 192.168.10.1 | Unknow | AXIS 210A or 211 Network Camera (Linux 2.6.17)   | 92       | webcam          | AXIS   | embedded | NULL  |
|  6 | 192.168.10.1 | Unknow | Linux 3.16                                       | 96       | general purpose | Linux  | Linux    | 3.X   |
|  7 | 192.168.10.1 | Unknow | ASUS RT-N56U WAP (Linux 3.4)                     | 95       | WAP             | Linux  | Linux    | 3.X   |
|  8 | 192.168.10.1 | Unknow | Linux 3.10 - 4.1                                 | 92       | general purpose | Linux  | Linux    | 4.X   |
|  9 | 192.168.10.1 | Unknow | Linux 3.1                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 10 | 192.168.10.1 | Unknow | Western Digital My Cloud DL4100 NAS (Linux 3.10) | 93       | general purpose | Linux  | Linux    | 3.X   |
| 11 | 192.168.10.1 | Unknow | Linux 3.10                                       | 93       | general purpose | Linux  | Linux    | 3.X   |
| 12 | 192.168.10.1 | Unknow | Western Digital My Cloud DL4100 NAS (Linux 3.10) | 93       | general purpose | Linux  | Linux    | 3.X   |
| 13 | 192.168.10.1 | Unknow | Linux 3.12 - 4.10                                | 96       | general purpose | Linux  | Linux    | 4.X   |
| 14 | 192.168.10.1 | Unknow | Linux 3.2                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 15 | 192.168.10.1 | Unknow | Linux 3.16                                       | 96       | general purpose | Linux  | Linux    | 3.X   |
| 16 | 192.168.10.1 | Unknow | DD-WRT v24-sp2 (Linux 3.10)                      | 93       | WAP             | Linux  | Linux    | 3.X   |
| 17 | 192.168.10.1 | Unknow | ASUS RT-N56U WAP (Linux 3.4)                     | 95       | WAP             | Linux  | Linux    | 3.X   |
| 18 | 192.168.10.1 | Unknow | Linux 3.10 - 4.1                                 | 92       | general purpose | Linux  | Linux    | 4.X   |
| 19 | 192.168.10.1 | Unknow | Linux 3.1                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 20 | 192.168.10.1 | Unknow | AXIS 210A or 211 Network Camera (Linux 2.6.17)   | 92       | webcam          | AXIS   | embedded | NULL  |
| 21 | 192.168.10.1 | Unknow | Linux 3.10                                       | 93       | general purpose | Linux  | Linux    | 3.X   |
| 22 | 192.168.10.1 | Unknow | Linux 3.16                                       | 96       | general purpose | Linux  | Linux    | 3.X   |
| 23 | 192.168.10.1 | Unknow | Linux 3.12 - 4.10                                | 96       | general purpose | Linux  | Linux    | 4.X   |
| 24 | 192.168.10.1 | Unknow | Western Digital My Cloud DL4100 NAS (Linux 3.10) | 93       | general purpose | Linux  | Linux    | 3.X   |
| 25 | 192.168.10.1 | Unknow | Linux 3.2                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 26 | 192.168.10.1 | Unknow | ASUS RT-N56U WAP (Linux 3.4)                     | 95       | WAP             | Linux  | Linux    | 3.X   |
| 27 | 192.168.10.1 | Unknow | Linux 3.10 - 4.1                                 | 92       | general purpose | Linux  | Linux    | 4.X   |
| 28 | 192.168.10.1 | Unknow | Linux 3.1                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 29 | 192.168.10.1 | Unknow | AXIS 210A or 211 Network Camera (Linux 2.6.17)   | 92       | webcam          | AXIS   | embedded | NULL  |
| 30 | 192.168.10.1 | Unknow | DD-WRT v24-sp2 (Linux 3.10)                      | 93       | WAP             | Linux  | Linux    | 3.X   |
| 31 | 192.168.10.1 | Unknow | AXIS 210A or 211 Network Camera (Linux 2.6.17)   | 92       | webcam          | AXIS   | embedded | NULL  |
| 32 | 192.168.10.1 | Unknow | Linux 3.16                                       | 96       | general purpose | Linux  | Linux    | 3.X   |
| 33 | 192.168.10.1 | Unknow | Linux 3.1                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 34 | 192.168.10.1 | Unknow | ASUS RT-N56U WAP (Linux 3.4)                     | 95       | WAP             | Linux  | Linux    | 3.X   |
| 35 | 192.168.10.1 | Unknow | Western Digital My Cloud DL4100 NAS (Linux 3.10) | 93       | general purpose | Linux  | Linux    | 3.X   |
| 36 | 192.168.10.1 | Unknow | Linux 3.10 - 4.1                                 | 92       | general purpose | Linux  | Linux    | 4.X   |
| 37 | 192.168.10.1 | Unknow | DD-WRT v24-sp2 (Linux 3.10)                      | 93       | WAP             | Linux  | Linux    | 3.X   |
| 38 | 192.168.10.1 | Unknow | Linux 3.12 - 4.10                                | 96       | general purpose | Linux  | Linux    | 4.X   |
| 39 | 192.168.10.1 | Unknow | Linux 3.2                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 40 | 192.168.10.1 | Unknow | Linux 3.2.0                                      | 92       | general purpose | Linux  | Linux    | 3.X   |
| 41 | 192.168.10.1 | Unknow | Linux 3.10 - 4.1                                 | 92       | general purpose | Linux  | Linux    | 4.X   |
| 42 | 192.168.10.1 | Unknow | Linux 3.12 - 4.10                                | 96       | general purpose | Linux  | Linux    | 4.X   |
| 43 | 192.168.10.1 | Unknow | Linux 3.1                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 44 | 192.168.10.1 | Unknow | Linux 3.2                                        | 93       | general purpose | Linux  | Linux    | 3.X   |
| 45 | 192.168.10.1 | Unknow | ASUS RT-N56U WAP (Linux 3.4)                     | 95       | WAP             | Linux  | Linux    | 3.X   |
| 46 | 192.168.10.1 | Unknow | Linux 3.16                                       | 96       | general purpose | Linux  | Linux    | 3.X   |
| 47 | 192.168.10.1 | Unknow | Linux 3.10                                       | 93       | general purpose | Linux  | Linux    | 3.X   |
| 48 | 192.168.10.1 | Unknow | AXIS 210A or 211 Network Camera (Linux 2.6.17)   | 92       | webcam          | AXIS   | embedded | NULL  |
| 49 | 192.168.10.1 | Unknow | Western Digital My Cloud DL4100 NAS (Linux 3.10) | 93       | general purpose | Linux  | Linux    | 3.X   |
| 50 | 192.168.10.1 | Unknow | DD-WRT v24-sp2 (Linux 3.10)                      | 93       | WAP             | Linux  | Linux    | 3.X   |
+----+--------------+--------+--------------------------------------------------+----------+-----------------+--------+----------+-------+
50 rows in set (0.00 sec)


mysql> select * from ssfingers;
+----+------+-------+---------+------------+---------+---------+-----------+------+
| id | port | state | reason  | name       | product | version | extrainfo | conf |
+----+------+-------+---------+------------+---------+---------+-----------+------+
|  1 |   53 | open  | syn-ack | tcpwrapped |         |         |           | 8    |
|  2 |   80 | open  | syn-ack | http       |         |         |           | 10   |
|  3 |  443 | open  | syn-ack | https      |         |         |           | 10   |
+----+------+-------+---------+------------+---------+---------+-----------+------+
3 rows in set (0.00 sec)

```

---
that's all
