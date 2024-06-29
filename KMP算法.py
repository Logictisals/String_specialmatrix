def get_next(pattern):
    # 初始化一个长度与模式字符串相同的列表 next ，并初始化为 0
    next = [0] * len(pattern)
    i = 1  # 从第二个位置开始处理
    len_ = 0  # 用于记录匹配的长度

    while i < len(pattern):  # 遍历模式字符串（除了第一个字符）
        if pattern[i] == pattern[len_]:  # 如果当前字符与当前匹配长度对应的字符相同
            len_ += 1  # 匹配长度增加
            next[i] = len_  # 更新 next 列表
            i += 1  # 移动到下一个位置
        else:  # 如果不相同
            if len_!= 0:  # 如果之前有匹配的部分
                len_ = next[len_ - 1]  # 回溯匹配长度
            else:  # 如果之前没有匹配的部分
                next[i] = 0  # 设置为 0
                i += 1  # 移动到下一个位置
    return next  # 返回计算好的 next 列表

def kmp_search(text, pattern):
    lps = get_next(pattern)  # 获取模式字符串的 next 列表
    i = 0  # 文本指针，从开头开始
    j = 0  # 模式指针，从开头开始

    while i < len(text):  # 遍历文本字符串
        if pattern[j] == text[i]:  # 如果当前字符匹配
            i += 1  # 文本指针移动
            j += 1  # 模式指针移动

            if j == len(pattern):  # 如果模式字符串完全匹配
                return i - j  # 返回匹配的起始位置
        else:  # 如果不匹配
            if j!= 0:  # 如果模式指针不是在开头
                j = lps[j - 1]  # 根据 next 列表回溯模式指针
            else:  # 如果模式指针在开头
                i += 1  # 文本指针移动
    return -1  # 未找到匹配返回 -1

# 测试
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(kmp_search(text, pattern))  # 输出匹配结果
# 测试
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(kmp_search(text, pattern))

def test_kmp_search(text, pattern):
    lps = get_next(pattern)
    i = 0
    j = 0
    print("匹配过程:")
    while i < len(text):
        print(f"当前比较: 文本字符 {text[i]}, 模式字符 {pattern[j]}")
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == len(pattern):
                print("匹配成功")
                return i - j
        else:
            print(f"不匹配，回溯: 模式指针从 {j} 回溯到 {lps[j - 1] if j!= 0 else 0}")
            if j!= 0:
                j = lps[j - 1]
            else:
                i += 1
    print("匹配失败")
    return -1
test_kmp_search(text,pattern)