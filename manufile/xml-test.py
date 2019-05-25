from bs4 import BeautifulSoup

xml = """
<Children>
    <Child>イチロー</Child>
    <Child>ジロー</Child>
    <Child>サブロー</Child>
</Children>
"""
soup = BeautifulSoup(xml)  # (1)html parse

for i in soup.find_all("child"):
    print(i.string)
