create database animeDB; use animeDB;
drop table if exists AnimeInfo;
create table AnimeInfo(MALID int not null , Name varchar(120) not null,Score float, EnglishName varchar(120), 
	JapaneseName varchar(100), Type char(8), Episodes int, Aired varchar(30), Aired_start date, Aired_end date, 
    Premiered VARCHAR(15), Source char(20), Duration VARCHAR(30),  hr_duration INT, min_duration INT, 
    Duration_in_min_per_episode INT, Rating Char(10), Ranked int, Popularity int, Members int, Favourites int, 
    Watching int, Completed int, OnHold int, Dropped int, PlanToWatch int,Score10 int,Score9 int, Score8 int,
    Score7 int,Score6 int,Score5 int,Score4 int,Score3 int,Score2 int,Score1 int,Synopsis longtext,
    PRIMARY KEY (MALID));
-- index on Aired_start
CREATE INDEX idx_duration ON AnimeInfo(Aired_start); 
load data local infile 'C:/Fall21/ECE656/project_dataset/anime1.csv' ignore into table AnimeInfo
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
(@col1, @col2,@col3, @col4,@col5, @col6,@col7, @col8,@col9, @col10,@col11, @col12,@col13, @col14,@col15, @col16,
	@col17, @col18,@col19,@col20,@col21, @col22, @col23, @col24,@col25, @col26,@col27, @col28,@col29, @col30, 
    @col31, @col32, @col33, @col34, @col35,@col36)
 set MALID = @col1, Name = @col2, Score = if(@col3 = 'Unknown', NULL, @col3), EnglishName = @col5, 
	 JapaneseName = @col6, Type = @col7, Episodes = if(@col8 = 'Unknown', NULL, @col8), Aired = @col9, 
     Aired_start = NULL, Aired_end = Null, Premiered = @col10, Source= @col14, Duration = @col15,
     -- converting null to 0 and then converting from hrs to mins
     hr_duration = regexp_replace(regexp_substr(Duration, '^[0-9]{1,2} hr'),' hr',''),
     min_duration = regexp_replace(regexp_substr(@col15,'[0-9]{1,2} min'),' min',''),
     Duration_in_min_per_episode = (coalesce(hr_duration*60,0) + coalesce(min_duration,0)),
	 Rating = regexp_substr(@col16,'(^R - 17\+)|(^PG-13)|(^PG)|(^R\+)|(G)|(^Rx)|(^Unknown)'), 
     Ranked= if(@col17 = 'Unknown', NULL, @col17),Popularity=@col18, Members= @col19, Favourites = @col20,
     Watching = @col21, Completed= @col22,OnHold= @col23, Dropped= @col24, PlanToWatch= @col25,
     Score10= if(@col26 = 'Unknown', NULL, @col26), Score9=if(@col27 = 'Unknown', NULL, @col27),
     Score8= if(@col28 = 'Unknown', NULL, @col28), Score7 = if(@col29 = 'Unknown', NULL, @col29),
     Score6= if(@col30 = 'Unknown', NULL, @col30), Score5 = if(@col31 = 'Unknown', NULL, @col31),
     Score4= if(@col32 = 'Unknown', NULL, @col32), Score3 = if(@col33 = 'Unknown', NULL, @col33),
     Score2= if(@col34 = 'Unknown', NULL, @col34), Score1= if(@col35 = 'Unknown', NULL, @col35),Synopsis = @col36;
update AnimeInfo set Aired_start = str_to_date(regexp_replace(regexp_substr -- converting into date format
			(Aired, '^[a-zA-Z]{3} [0-9]{1,2}, [0-9]{4}'),',' ,''),"%M %d %Y");
update AnimeInfo set Aired_end = str_to_date(regexp_replace(regexp_substr(regexp_substr
			(Aired, 'to [a-zA-Z]{3} [0-9]{1,2}, [0-9]{4}$'),'[a-zA-Z]{3} [0-9]{1,2}, [0-9]{4}$'),',',''),"%M %d %Y");
update AnimeInfo set hr_duration = 0 where hr_duration is NULL;
update AnimeInfo set Rating = NULL where Rating ='Unknown';
update AnimeInfo set Premiered = NULL where Premiered ='Unknown';
update AnimeInfo set Source  = NULL where Source ='Unknown';
update AnimeInfo set Duration_in_min_per_episode = NULL where Duration_in_min_per_episode=0;
Alter table AnimeInfo drop Aired,drop Duration,drop hr_duration, drop min_duration;
ALTER TABLE animeinfo ADD CONSTRAINT CHK_Score CHECK (Score>=0 and Score<=10);
ALTER TABLE animeinfo ADD CONSTRAINT CHK_Episodes CHECK (Episodes>0);
ALTER TABLE animeinfo ADD CONSTRAINT CHK_Duration CHECK (Duration_in_min_per_episode>0);
ALTER TABLE animeinfo ADD CONSTRAINT CHK_MALID CHECK (MALID>0);
drop view if exists Anime_View_NonRegUser;
create view Anime_View_NonRegUser As (select Name, JapaneseName, Rating, Score, EnglishName, 
			Episodes, Aired_start, Duration_in_min_per_episode from animeinfo);


