create schema mydb collate utf8mb4_general_ci;
use mydb;

create table user
(
    id         bigint unsigned primary key auto_increment,
    name       varchar(50)  not null comment '유저의 실제이름',
    password   varchar(100) not null comment '이 예제에선 plain text로 저장한다. 실제론 sha256 같은 해시화를 통해 저장해야 한다.',
    nick       varchar(20)  not null comment '유저의 닉네임',
    email      varchar(100) not null comment '유저 이메일. 반드시 있어야 한다.',
    phone_num  varchar(13)  null comment '핸드폰이 없어도 가입 할 수 있다.',
    created_dt datetime     not null default current_timestamp(),
    updated_dt datetime     not null default current_timestamp()
) collate utf8mb4_general_ci;

create table board
(
    id         bigint unsigned primary key auto_increment,
    user_id    bigint unsigned not null comment 'user 테이블 id 컬럼',
    title      varchar(255)    not null comment '게시글 제목',
    created_dt datetime        not null default current_timestamp(),
    updated_dt datetime        not null default current_timestamp()
) collate utf8mb4_general_ci;


create table board_content
(
    id         bigint unsigned primary key auto_increment,
    board_id   bigint unsigned not null comment 'board 테이블 id 컬럼',
    content    longtext        not null comment '게시글 상세 내용',
    created_dt datetime        not null default current_timestamp(),
    updated_dt datetime        not null default current_timestamp()

) collate utf8mb4_general_ci;


alter table user add constraint user_unq unique (email);
alter table board_content add constraint board_content_uq unique (board_id);

insert into user (name, nick, email, phone_num)
values ('홍길동', 'Hero Hong', 'father-is-not-father@gmail.com', '010-1234-1234')


