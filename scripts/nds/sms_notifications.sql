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
  Response        NVARCHAR(MAX),
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

/*
--SMS Notifications
SELECT [Id], CONVERT(DATE, [Date]) [Date], JSON_VALUE([Response], '$.status') [Status], JSON_VALUE([Response], '$.code') [Code], JSON_VALUE([Response], '$.message') [Message], JSON_VALUE([Response], '$.summary._id') [_Id], JSON_VALUE([Response], '$.summary.message_id') [MessageId], JSON_VALUE([Response], '$.summary.type') [Type], JSON_VALUE([Response], '$.summary.total_sent') [TotalSent], JSON_VALUE([Response], '$.summary.contacts') [Contacts], JSON_VALUE([Response], '$.summary.total_rejected') [TotalRejected], JSON_VALUE([Response], '$.summary.numbers_sent[0]') [NumbersSent], JSON_VALUE([Response], '$.summary.credit_used') [CreditUsed], JSON_VALUE([Response], '$.summary.credit_left') [CreditLeft], JSON_VALUE([Response], '$.summary.wallet_used') [Wallet Used], [API] FROM [PracticeDB].[dbo].[SMSNotifications] 
*/