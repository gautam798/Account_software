policy of software :-
we have to connect database (like mysql,oracle).It can be used as personal accounting software
*guidelines*
#income section columns
i_date, i_type, i_reciever, i_sender, i_amount, i_reference
#expense section columns
e_date,e_type,e_exptype,e_reciever,e_sender,e_amount,e_reference
#asset section column
a_date,a_type,a_broker,a_taxes,a_status,a_amount,a_reference
#liability section column
l_date, l_type, l_loaner, l_intamount, l_intrest, l_amount, l_reference

date section is only supported in following format
YYYY-MM-DD  (eg:- 2021-11-15)

income section
following are option available
Type      :- Neft/Imps/Upi/Cash/Cheque
Reciever  :- axis/sbi/CASH
Sender    :- Any third party (mention details in reference)
amount    :- ANy integer amount (dont use decimals ,put it in reconcilation)
reference :- details of transaction

expense section
following are option available
Type        :-Neft/imps/upi/CASH
exptype     :-party /essential/urgent/debt/asset/other(mention details)
reciever    :-any third party
Sender      :-  axis/sbi/CASH
amount      :-  any int
reference   :-details of transaction

asset section
type      :- Gold / Stock / MF / bond
broker    :- any broker you have
taxes     :- int value
status    :- holding/sold
amount    :- int value
reference :- details of transaction

liability section
type       :-Personal/credit/other
loaner     :- any firms
intamount  :- int amount
intrest    :-int amount
amount     :-int amount
reference  :-details of transaction(like emi's)
