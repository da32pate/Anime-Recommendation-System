drop table if exists AnimeRatingComplete;
create table AnimeRatingComplete(UserID int not null,MALID int not null,rating int not NULL);
load data local infile 'C:/Fall21/ECE656/project_dataset/rating_complete.csv' ignore 
		into table AnimeRatingComplete
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines
(UserID,MALID,Rating);
ALTER TABLE AnimeRatingComplete ADD CONSTRAINT PK_AnimeRatingComplete PRIMARY KEY (UserID,MALID);
ALTER TABLE animeratingcomplete ADD CONSTRAINT FK_animeratingcomplete_watchstatus 
			FOREIGN KEY (UserID) REFERENCES animeuserratingwatchstatus(UserID)on delete cascade;
ALTER TABLE animeratingcomplete ADD CONSTRAINT FK_animeratingcomplete_watchstatus1
			FOREIGN KEY (MALID) REFERENCES animeuserratingwatchstatus(MALID)on delete cascade;
ALTER TABLE animeratingcomplete ADD CONSTRAINT CHK_rating CHECK (rating>=0 and rating<=10);








