drop table movie;

create table movie(id number, 
                   movieNm varchar2(255),
                   directorNm varchar2(255),
                   openDt date,
                   showTm number,
                   nationNm varchar2(200),
                   genreNm varchar2(200),
                   watchGradeNm varchar2(50),
                   companyNm varchar2(255),
                   ori_lang varchar2(100),
                   budget number,
                   actor nclob,
                   staff nclob,                  
                   series number,
                   keywords varchar2(255),
                   awards varchar2(255),
                   naver_cmt nclob,
                   naver_cmt_nn number,
                   naver_pre_eval number,
                   naver_ex_pt number,
                   ori_book number,                   
                   plot nclob,
                   audiAcc number);

                 
select * from movie;


