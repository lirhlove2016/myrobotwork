# -*- coding:utf8 -*-

# ------------------------------ admin login url     ---------------------
ADMIN_API = {
    "fsdregister":"/flyHandApp/api/user/loginTest",
    "fsduserpassword":"/flyHandApp/api/user/loginAdd",
    "fsdlogin":"/flyHandApp/api/user/loginPassword",
    "fsdcheckaccount":"/flyHandApp/api/user/checkAccountRegisted",
    "fsdsms":"/flyHandApp/api/user/getSmsCheckCode?phone=test",
    "addtools":"/flyHandApp/api/user/addTool/v1?userId=id&token=TOKEN",
    "syslogin":"/management/sys/login",
    "freezeflyaccount":"/management/user/updateFlyUserAccountState",
	"queryflyorderlist":"/management/order/queryFlyOrderList",
    }

API_YWB_URL={
	"addorder":"/businessTreasure/api/order/addOrderQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"ywblogin":"/businessTreasure/api/user/loginP",
	"salesmanquery":"/businessTreasure/api/user/salesmanQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"cropsAllQuery":"/businessTreasure/api/tool/cropsAllQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"addorder":"/businessTreasure/api/order/addOrderQuery?access_phone=PHONE&userId=id&token=TOKEN",
	

}




