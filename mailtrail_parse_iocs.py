import sys
import os

def get_iocs_from_txt(all_files):
    for path in all_files:
        print(all_files[path])
        
        with open('mailtrail_iocs.txt','a',encoding='utf-8') as d:
            virustype = path.split('.')[0]
            print(virustype)
            d.write('['+virustype+']'+'\n')
            with open(all_files[path],'r',encoding='utf-8') as f:
                lines = f.readlines()
                url_list = []
                for line in lines:
                    if line.strip()[0:1]=='#' or line.strip()=='' or line.strip()[0:1]=='/':
                        continue
                    if line.strip()[0:4]=='http':
                        print('[URL]')
                        print(line.strip())
                        d.write(line)
                        url_list.append(line.strip('\n'))
                    else:
                        print(line.strip())
                        d.write(line)
                f.close()
            d.close()

def get_file(root_path, all_files={}):
    '''
    递归函数，遍历该文档目录和子目录下的所有文件，获取其path
    '''
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            all_files[file] = root_path + '/' + file
        else:  # is a dir
            get_file((root_path+'/'+file), all_files)
    return all_files


if __name__ == '__main__':
    path = './malware'
    all_files = get_file(path)
    get_iocs_from_txt(all_files)
    