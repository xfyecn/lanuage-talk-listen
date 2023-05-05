import random

academic_scenes = ['建筑', '工业设计/艺术', '城市规划', '手工艺品（编织、针织、织物、家具、雕刻、马赛克、陶瓷、民间艺术）', '洞穴/岩画', '音乐和音乐史', '摄影', '文学和作家', '书籍、报纸、杂志、期刊', '动植物灭绝或保护行动', '鱼类和其他水生生物', '细菌和其他微生物', '医学技术', '公共卫生', '感官器官的生理学', '生物化学', '动物行为（迁徙、觅食、防御）', '栖息地及其对动植物的适应性', '营养及其对身体的影响', '动物交流', '天气和大气', '海洋学', '冰川、冰川地形、冰河时期', '沙漠和其他极端环境', '污染、替代能源、环境政策', '其他行星的大气', '天文学和宇宙学', '光学性质、光学', '声学特性', '电磁辐射', '粒子物理学', '电视、广播、雷达技术', '无机物质的化学', '计算机科学', '地震学（板块结构、地震、构造）']
school_scenes = {
    "学校食堂场景":['饭菜好不好吃','食堂的优惠政策','卫生安全','食堂政策'],
    "学校宿舍场景":['宿舍的安排','学生校外租房','房间设施问题','室友之间相处问题','宿舍政策/管理制度'],
    "学校图书馆场景":['找不到想借的书','还书过期','图书馆准备考试复习','准备论文','图书馆的基本部门设置和常见设施','查询资料','借书还书','买书','美国大学图书馆的基本制度','借书还书相关以及遇到的各种问题'],
    "学校假期场景":['假期去哪玩','回忆假期去过哪玩','有什么好玩的'],
    "学校办公室场景":['上课请假','延期交作业','论文准备','选课咨询','论文选题','论文写作','关于论文问题','其他活动申请'],
    "学生注册场景":['开学注册问题','缴费问题','毕业需求','课程学分计算','报到注册的时间','报到注册的准备材料','报到注册可能遇到的问题'],
    "学术选课场景":['选课问题','选课困难','学生选课太多跟不上','退课和放弃课程','学生对自己情况的分析'],
    "学校维护场景":['教室的桌椅损坏','宿舍的物品损坏','维护时间协商'],
    "学生勤工俭学场景":['兼职工作',"与课程时间冲突，协调工作时间","招聘应聘",'参加 career fair','工作条件/工资相关','工作待遇和时间'],
    "学校奖学金场景":['奖学金申请','奖学金问题',"咨询奖学金的种类","奖学金授予的资格","奖学金申请的材料","申请到奖学金的可能性"],
    "学校社团场景":['场地申请','社团申请','社团招生','社团活动','社团问题','社团设立、改动','社团场所'],
    "学校课程场景":["涉及课堂内容，比如学生没有听懂课下讨论上课的某一问题","讨论老师教学质量","讨论课堂留下的作业","安排考试","调课事宜","课程辅助材料","考试复习","课程（课程目的；课程类型；课程形式；课程作业）","作业类型；作业方法；交作业相关","论文分数","学生由于迟到或者旷课而向另外一个学生询问上课的内容","迟到或者旷课理由",],
    "学生转学场景":['转学或者转专业理由','学生转学的特殊情况','转学申请流程'],
    "学生组织活动场景":['学生经常参加和组织的活动','活动的目的','活动的具体内容'],
    "学校医院场景":["学生看病"],

}



scene = {
    "词汇题":'按照新托福阅读词汇题模式，对{}单词生成英语阅读短文、问题（{}在短文中跟以下选项那个意思相近？）、生成四个选项，不需要生成选项答案。',
    "词汇阅读":"用这些单词({})生成一篇阅读理解文章",
    "英语对话":"Let's talk about {}.",
    "随机话题":"Can you give a randomly topic to me.",
    "讲座": "新托福听力阅读为模板。以{}为主题，生成一篇大学教授给学生讲课的文章。文章中会涉及到具体的例子，以及教授会对例子进行具体说明。",
    "单词分析":"对{}单词进行详细分析，包括词根词缀、单词含义以及对应的使用例子。",
    "扮演角色":"我想让你扮演我的{}，根据你的角色职责使用英语向我提问一个问题。如果你不确定具体角色设定，可以参考现实生活生成角色背景。",
    "阅读题目":"根据新托福阅读理解文章的选择题类型，生成五道选择题，不需要生成答案。",
    "阅读答案":"根据上面选择题，生成答案和解释。",
    "学校":"根据新托福听力模板，生成{}的英语对话，内容包括{}等话题，两人讨论话题会延申到其他{}话题上面。两人对话分别用P1:和P2:表示。对话内容不少于30段。",
    "语法批改":"Help me check if there are any English grammar errors in these contents: {}"

}

toefl_scenes = {
    "oral_task2":[
    '根据新托福口语题目中TASK2类型，生成大学将要实施某个政策并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
    '根据新托福口语题目中TASK2类型，生成大学将要实施某个程序并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
    '根据新托福口语题目中TASK2类型，生成大学将要实施某个规则并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
    '根据新托福口语题目中TASK2类型，生成大学将要实施某个计划并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
    '根据新托福口语题目中TASK2类型，生成大学将要对校园设施做某事并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
    '根据新托福口语题目中TASK2类型，生成大学做某事会提升或者降低校园生活质量的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
],

}






