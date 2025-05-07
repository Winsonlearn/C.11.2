

create table admin (adminid varchar(10) primary key, USERNAME varchar(128), PASSWORD mediumtext, LAST_LOGIN varchar(40), ROLE varchar(15), FULLNAME varchar(128), JENKEL CHAR(1), NO_TELP varchar(20), ALAMAT mediumtext, PHOTO MEDIUMTEXT, DTE_CREATED DATE);


create table anggota (idanggota varchar(10) primary key, adminid varchar(10), FULL_NAME varchar(128), TMP_LAHIR varchar(90), TGL_LAHIR varchar(20), ALAMAT MEDIUMTEXT, jk CHAR(1), TELP varchar(20), FOTO MEDIUMTEXT, D_CREATED DATE, FOREIGN KEY (adminid) REFERENCES admin(adminid));

create table perpus (ID_PERPUS int primary key, NAMA_P varchar(128), ALAMAT_P MEDIUMTEXT, ABOUT MEDIUMTEXT);

CREATE table buku (bukuid varchar(10) primary key, adminid varchar(10), TITLE varchar(150), AUTHOR varchar(128), PUBLISHER varchar(128), YEAR CHAR(4), QTY INT, KELUAR INT, FOREIGN KEY (adminid) REFERENCES admin(adminid));

CREATE TABLE peminjaman (pinjamid varchar(10) primary key, idanggota varchar(10), adminid varchar(10), TGL_PINJAM DATE, JML_BUKU INT, STATS varchar(20), FOREIGN KEY (idanggota) REFERENCES anggota(idanggota), FOREIGN KEY (adminid) REFERENCES admin(adminid));

create TABLE detail_pinjam (dipinjamid INT primary key auto_increment, pinjamid varchar(10), bukuid varchar(10), TGL_KEMBALI DATE, DENDA INT, STATUS varchar(20), FOREIGN KEY (pinjamid) REFERENCES peminjaman(pinjamid), FOREIGN KEY (bukuid) REFERENCES buku(bukuid));

CREATE TABLE notif (ID_NOTIF int primary key auto_increment, adminid varchar(10), JUDUL varchar(128), ISI varchar(128), DT DATE, FOREIGN KEY (adminid) REFERENCES admin(adminid));