--create SMSNotifications table:
use PracticeDB
go

--drop and create table if exists:
if exists 
  (select * from sys.tables
   where name = 'SMSNotifications')
drop table SMSNotifications
go

create table SMSNotifications
(
	Id              int not null identity(1,1),
  [Date]         	datetime not null default getdate(),
  Response        text NULL,
  API             varchar(25) not null,

constraint PKIdSMSNotifications primary key clustered(Id)
)
go

--drop and re-create index if exists else create:
if exists
  (select * from sys.indexes 
   where name = 'SMSNotificationsDate' 
   and object_id = object_id('SMSNotifications'))
drop index SMSNotifications.SMSNotificationsDate
go

create index SMSNotificationsDate
  on SMSNotifications([Date])
go

if exists
  (select * from sys.indexes 
   where name = 'SMSNotificationsAPI' 
   and object_id = object_id('SMSNotifications'))
drop index SMSNotifications.SMSNotificationsAPI
go

create index SMSNotificationsAPI
  on SMSNotifications(API)
go