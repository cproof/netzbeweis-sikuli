urls = findAll(Pattern("1650484649132.png").targetOffset(-62,-1))
for url in urls:
    sleep(1)
    click(url)
    sleep(0.2) 
    type("c", KEY_CTRL)
    click("1650484745358.png")
    click("1650484765338.png")
    click("1650485681973.png")
    type("v", KEY_CTRL)
    type(Key.HOME)
    type(Key.DELETE)
    type(Key.DELETE)
    type(Key.ENTER)
    wait("1650485198779.png", FOREVER)
    click("1650485213238.png")
    click("1650485232881.png")
    wait("1650485781530.png", FOREVER )
    click("1650485282618.png")
    click("1650486214416.png")



    