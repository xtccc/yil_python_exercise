'''给大家出一道python练习题， 大家有空时可以试试实现一下。要求封装成class，限时1个小时。
编写脚本，统计result.log中的XXX Error开头关键字的数量和总数，忽略大小写。
数据示例:
    SQL_Format Error: Please check your SQL ....
    Script error: script performance.sh can not find...
输出:  
    SQL_Format Error: 1
    Script error: 1
    Total: 2
    '''
'''    SQL_Format Error: 6
    Script error: 5
    Total: 11'''
class find_error():
    def find_error_num(self,log_file):
        # return error num
        #log_file  = 'result.log'
        with open(log_file ,'r') as f :
            lines = f.readlines( )
        error_name_dict = {}
        for line in lines:
            error = line.split()[1]
            if error.lower() == "error:":
                error_name = line.split()[0]
                # 循环error_name 用于找出erro_name是否存在于dict中，不再的创建dict.key 在的value+1
                if error_name in error_name_dict.keys():
                    error_name_dict[error_name] += 1 
                else:
                    error_name_dict[error_name] = 1
        sum_error=0
        for key in error_name_dict:
            print("{} error:{}".format(key,error_name_dict[key]) )
            sum_error+=error_name_dict[key]
        print("total error:{}".format(sum_error))

#find_error_num('result.log')
a = find_error()
a.find_error_num('result.log')