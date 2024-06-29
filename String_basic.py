class String:
    def __init__(self, content=''):
        self.content = content

    def __str__(self):
        return self.content

    def concat(self, str_to_concat):
        """
        串接操作，将另一个字符串连接到当前字符串的末尾。
        :param str_to_concat: 要连接的字符串
        """
        self.content += str_to_concat

    def substring(self, start, end):
        """
        截取子串。
        :param start: 子串的起始索引（包含）
        :param end: 子串的结束索引（不包含）
        :return: 截取的子串
        """
        return self.content[start:end]

    def find(self, str_to_find):
        """
        查找子串的位置。
        :param str_to_find: 要查找的子串
        :return: 子串的位置，如果未找到返回-1
        """
        position = self.content.find(str_to_find)
        return position

# 测试串的方法
def test_string():
    # 创建字符串
    original_str = String("Hello World")
    print("原始字符串:", original_str)

    # 串接操作
    original_str.concat(" in Python")
    print("串接后的字符串:", original_str)

    # 截取子串
    sub_str = original_str.substring(6, 11)
    print("截取的子串:", sub_str)

    # 查找子串
    position = original_str.find("World")
    print("子串 'World' 的位置:", position)

    # 查找不存在的子串
    not_found_position = original_str.find("宇宙")
    print("子串 '宇宙' 的位置:", not_found_position)

test_string()