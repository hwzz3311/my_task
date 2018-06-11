#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:HW 
@file: three_level_menu.py 
@time: 2018/06/07 
"""

city_info= {
    "山东省":{
        "济南":[
            "历城区",
            "长清区",
        ],
        "菏泽":[
                "曹县",
            ]
        },
    "江苏省":{
        "南京":[
            "江宁区",
        ],
        "苏州":[
                "吴中区",
            ]
        }
}


province = "无"
city = "无"
while True:
    for province_key in city_info.keys():
        print(province_key)
    print("".center(30,"-"))
    if province == "无":
        province = input("\033[0;33m请从以上省份选择或按q退出\033[0;0m").strip()
    if city_info.get(province):
        while True:
            print("".center(30, "-"))
            print("\033[0;33m以下将为您显示%s的市级\033[0;0m"%province)
            for pro_key in city_info[province].keys():
                print(pro_key)
            if city is "无":
                city = input("\033[0;33m请继续选择%s的市级或者按q退出当前省份\033[0m"%province).strip()
            if city_info[province].get(city):
                for district in city_info[province][city]:
                    print(district)
                print("\033[0;33m\t{province}的{city}下的县/区已经为您显示完毕\033[0m".format(province = province,city = city))
                input("按Enter键继续")
                city = "无"
            elif city == "q":
                city = "无"
                break
            else:
                print("\033[0;31m\t输入错误，请重新输入！\033[0;0m")
                city = "无"
        province = "无"
    elif province == "q":
        break
    else:
        print("\033[0;31m\t输入错误，请重新输入！\033[0;0m")
        province = "无"
