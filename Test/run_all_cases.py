# coding : utf-8
# 主题：按测试模块，实现最多文件夹数的并发执行
# 问题：报告中各脚本的结果重叠了
import os, time
import unittest
import HTMLTestRunner
import threading
import multiprocessing

class TestResult(object):
    
    def create_suite(self):
        run_dir = '.\\test_case'
        case_dir = [x for x in os.listdir(run_dir)]
        #print(case_dir)
        # 初始化测试集（空列表）
        suite = []
        #应用unittest.TestSuite()类，创建一个测试容器
        for n in case_dir:
            testunit = unittest.TestSuite()
            unittest.defaultTestLoader._top_level_dir = None
            #discover方法定义
            discover = unittest.defaultTestLoader.discover(run_dir + '\\' + str(n), pattern = 'start_*.py', top_level_dir = None)
            #discover方法筛选出来的用例，循环添加到测试套件中
            for test_suite in discover:
                for test_case in test_suite:
                    testunit.addTest(test_case)
            suite.append(testunit)
        return suite, case_dir
    
    def run_suite(self):
        #调用create_suite()方法
        allTest = self.create_suite()

        now = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
        #定义报告存放路径，支持相对路径
        report = '.\\test_report\\'+ now +'_API_Result.html'
        fp = open(report,'wb')
        
        proc_list = []
        s = 0

        for item in allTest[0]:
            print(item)
            #定义测试报告
            runner = HTMLTestRunner.HTMLTestRunner(
                                    stream = fp,
                                    title = u'测试报告',
                                    description = u'用例执行情况:',
                                    verbosity = 0)
            #执行测试用例
            #result = runner.run(allTest)
            proc = threading.Thread(target = runner.run, args = (item,))
            proc_list.append(proc)
            s = s + 1

        for proc in proc_list:
            proc.start()
        for proc in proc_list:
            proc.join()
        fp.close()

if __name__ == '__main__':
    TestResult().run_suite()