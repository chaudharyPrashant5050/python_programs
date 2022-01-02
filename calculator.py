#!/usr/bin/env python
# coding: utf-8

# In[36]:


find_result = input()
numberAndOperatorList = []

current_num = ""

for i in find_result:
    if(i.isdigit() or i == '.'):
        current_num = current_num + i
    else:
        numberAndOperatorList.append(current_num)
        current_num = ""
        numberAndOperatorList.append(i)
    
numberAndOperatorList.append(current_num)
for i in numberAndOperatorList:
    print(i,end=" ")
    
    


# In[37]:


result = 0
le = len(numberAndOperatorList) - 1
i = 0
operator = ""

new_list = []
div_mul_flag = 0

while(i<=le):
    element = numberAndOperatorList[i]
    
    if(element == '/' or element == 'x'):
        
        if(div_mul_flag):
            if(element == '/'):
                result = (new_list[len(new_list)-1]) // int(numberAndOperatorList[i+1])
            else:
                 if(element == 'x'):
                    result = (new_list[len(new_list)-1]) * int(numberAndOperatorList[i+1])
        else:    
            if(element == '/'):
                result = int(numberAndOperatorList[i-1]) / int(numberAndOperatorList[i+1])
            if(element == 'x'):
                result = int(numberAndOperatorList[i-1]) * int(numberAndOperatorList[i+1])
            
        new_list.pop()
            
        i = i+2
        new_list.append((result))
        div_mul_flag = 1
    else:
        new_list.append(element)
        i = i+1
        div_mul_flag = 0
        
for i in new_list:
    print(i,end=" ")
        
result = int(new_list[0])
le = len(new_list) - 1
i = 1
operator = ""

            


while(i<le):
    
    operator = new_list[i]
    
    if(operator == '+'):
        result = result+int(new_list[i+1])
    elif(operator == '-'):
        result = result-int(new_list[i+1])
    
    i = i+2
    
    
    
print()
    
print(result)


# In[ ]:




