# App-Usability-AB-Test
基于Python的App界面可用性A/B测试数据分析（和D老师学习版）
Python-based App Interface Usability A/B Test Data Analysis (Learned with Teacher D)

【项目背景 / Project Background】
为了对比传统界面（A）和优化界面（B）到底哪个更好用，我们找了 60 名用户，收集了他们在两个界面上操作的 120 条测试记录。
To compare the traditional interface (A) with the optimized interface (B) to see which one is better, we recruited 60 users and collected 120 interaction test records from both interfaces.

【用到的工具 / Tools Used】
主要用了 Python 的 Pandas 库来处理数据，最后把代码上传在了 GitHub 上。
Mainly used Python's Pandas library for data processing, and uploaded the code to GitHub.

【我做了哪些事 / What I Did】
第一步是数据清洗。我发现满意度那一列缺了 3 个数据，我用了这列的中位数把它们补齐了。同时，我把 0 和 1（代表失败和成功），加了一列转成了中文标签（用 `map`），看起来更直观。
First step was data cleaning. I found 3 missing values in the satisfaction column and filled them with the median. Meanwhile, I mapped the 0s and 1s (representing failure and success) to Chinese labels using `map`, making it more intuitive.

第二步是数据分析。因为有些用户任务没做完（也就是失败了），他们只花了十几秒就放弃了。所以在计算平均耗时的时候，我把这 12 条失败记录给剔除掉了，不然会把整体平均时间给拉低，导致数据“虚假繁荣”。
Second step was data analysis. Because some users didn't finish the task (failed) and gave up after just a dozen seconds, I excluded these 12 failed records when calculating the average time. Otherwise, it would lower the overall average time, leading to "false prosperity" in the data.

【得出了什么结论 / Conclusions】
分析完我发现，A 和 B 两个界面的任务成功率打平，都是 90%。
After analysis, I found that interfaces A and B tied in task success rate, both at 90%.

但是！B 界面的效率高得多，平均耗时只要 62 秒，比 A 界面快了 16%。而且 B 界面的操作失误率直接降了 57%，用户点击屏幕的次数也少了 22%。在满意度打分上，B 界面也拿了更高的分数（5.28分 对比 4.38分）。
However! Interface B was much more efficient, with an average time of only 62 seconds, 16% faster than A. Moreover, B's operation error rate dropped by 57%, and users clicked the screen 22% fewer times. In terms of satisfaction scores, B also got a higher score (5.28 vs 4.38).

【我的业务建议 / Business Advice】
所以我给出的结论是：建议公司直接全量上线 B 界面。因为它不仅没降低成功率，还能让用户操作得更快、错得更少、心情更好。
So my conclusion is: I recommend the company to fully launch Interface B. Because it not only doesn't lower the success rate, but also lets users operate faster, make fewer mistakes, and feel better.

---
This is my first python project, good good study, day day up.
