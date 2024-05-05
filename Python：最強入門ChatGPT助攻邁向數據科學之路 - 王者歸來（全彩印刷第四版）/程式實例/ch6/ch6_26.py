# ch6_26.py
cars = ['honda','bmw','toyota','ford']     
print(f"目前串列car內容 = {cars}")
print("使用sorted()由小排到大")
cars_sorted = sorted(cars)            
print(f"從小排到大的排序串列結果 = {cars_sorted}")
print("-"*60)
print(f"原先串列car內容 = {cars}")
cars_sorted = sorted(cars,reverse=True)            
print(f"從大排到小的排序串列結果 = {cars_sorted}")
print(f"原先串列car內容不變 = {cars}")
print("="*60)
nums = [5, 3, 9, 2]     
print(f"目前串列num內容 = {nums}")
print("使用sorted()由小排到大")
nums_sorted = sorted(nums)            
print(f"從小排到大的排序串列結果 = {nums_sorted}")
print("-"*60)
print(f"原先串列num內容 = {nums}")
nums_sorted = sorted(nums,reverse=True)            
print(f"從大排到小的排序串列結果 = {nums_sorted}")
print(f"原先串列num內容不變 = {nums}")

    
