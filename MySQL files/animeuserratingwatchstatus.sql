drop table if exists AnimeUserRatingWatchStatus;
create table AnimeUserRatingWatchStatus(UserID int not null,MALID int,Rating int, WatchingStatus INT, 
			WatchedEpisodes int);
load data local infile 'C:/Fall21/ECE656/project_dataset/animelist1.csv' ignore into table 
		AnimeUserRatingWatchStatus
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines
(UserID,MALID,Rating,WatchingStatus,WatchedEpisodes);
ALTER TABLE animeuserratingwatchstatus ADD CONSTRAINT 
			PK_animeuserratingwatchstatus PRIMARY KEY (UserID,MALID);
ALTER TABLE animeuserratingwatchstatus ADD CONSTRAINT 
			FK_watchstatus_userinfo FOREIGN KEY (UserID) REFERENCES userinfo(UserID)on delete cascade;
ALTER TABLE animeuserratingwatchstatus ADD CONSTRAINT 
			FK_watchstatus_animeinfo FOREIGN KEY (MALID) REFERENCES animeinfo(MALID)on delete cascade;
            
            
            
            


