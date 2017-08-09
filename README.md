# hellopython
需求：获取目标网址的中每一天的水情公报，并保存进excel进行下一步处理。
分析水情公报url知，
http://www.sxmwr.gov.cn/gb-zxfw-news-3-list-79501 中，list后数字并非序列，不规范。因此需要先抓取水情公报栏目每一页所有天的水情公报链接，然后，进入每一链接抓取公报内容存储为本地文件。
详细步骤参考：
http://www.jianshu.com/p/eacde7b9cce2
以下分4步完成：
###1、获取每一天的公报链接（index.py)###
对于新手来说，感觉还是beautifulSoup抓取页面比较好用。（具体用法自行百度）
print结果如下
```    
gb-zxfw-news-3-list-62331
gb-zxfw-news-3-list-62314
……
```
###2、用excel处理上一步结果###
由于下一步需要一个list，形如['a','b']，于是将上一步运行结果，通过复制转置为一行，在下一行插入公式(假设第一行第一列为A1，此公式是为上一行每一个数据加上引号）
```
="'"%A1%"'"
```
然后另存为带逗号的csv格式，可以用记事本打开复制到下一个python程序中。
###3、存储每一天的公报为xls格式(content.py)###
###4、合并所有xls为多sheet表格###
在网上直接扒了一个vba代码：
```
Sub CombineWorkbooks()
Dim FilesToOpen, ft
Dim x As Integer
Application.ScreenUpdating = False
On Error GoTo errhandler
FilesToOpen = Application.GetOpenFilename _
(FileFilter:="Micrsofe Excel文件(*.xls), *.xls", _
MultiSelect:=True, Title:="要合并的文件")
If TypeName(FilesToOpen) = "boolean" Then
MsgBox "没有选定文件"
'GoTo errhandler
End If
x = 1
While x <= UBound(FilesToOpen)
Set wk = Workbooks.Open(Filename:=FilesToOpen(x))
wk.Sheets().Move after:=ThisWorkbook.Sheets _
(ThisWorkbook.Sheets.Count)
x = x + 1
Wend
MsgBox "合并成功完成！"
errhandler:
'MsgBox Err.Description
'Resume errhandler
End Sub
```
