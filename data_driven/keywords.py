from data_driven.steps import steps

# 关键字定义，通过关键字匹配对应的方法。 可根据需要新增对应的关键字和对应方法。
def get_keyword(driver,keyword,para_list):
    if keyword in ['Chrome','Firefox']:
        return steps().init_driver(keyword)
    elif keyword=='前往':
        return steps().get(driver,para_list)
    elif keyword=='填写':
        return steps().fill(driver,para_list)
    elif keyword=='点击':
        return steps().click(driver,para_list)
    elif keyword=='验证文字':
        return steps().assert_text(driver,para_list)
    elif keyword=='验证标题':
        return steps().assert_title(driver,para_list)

# 执行方法，逐个步骤转换为对应的关键字方法，并执行
def run(case):
    step_list = case.split(',')
    driver = get_keyword('',step_list[0],[])
    step_list.remove(step_list[0])
    for step in step_list:
        keyword, para_list = step.split('|')[0],step.split('|')[1].split('@@')
        get_keyword(driver,keyword,para_list)
    driver.get_screenshot_as_png()
    driver.quit()

