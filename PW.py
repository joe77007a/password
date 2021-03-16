chance = 3
while chance > 0:
	    password_input = input('請輸入密碼')
	    password = '420'
	    chance = chance - 1
	    if password_input == password:
	            print('登入成功！')
	            break
	    elif chance > 0:
	    	    print('密碼錯誤！ 還有', chance, '次機會')
	    else:   
	    	    print('登入失敗')