# Sorting
<p> Basically there are 5 sorting algorithm and rest are derived from them.</p>
1. Insertion Sort<br>
1. Bubble Sort<br>
1. Selection Sort<br>
1. Merge Sort<br>
1. Quick Sort<br>
<hr>

## 1. Insertion Sort
<p>In **insertion sort**, we use two loop generally i.e <br>
<pre>
1. for loop: Started from position ~~0~~ 1
|    2. while loop(nested)
</pre>
In this sorting algorithm the given array is getting sorted upto the position of first iteration. The elements antecedent that position is sorted. For next iteration the pointer move to next element and the array get sorted upto that position and its goes on. The for loop commit **n-1** iteration and while loop did **i-1** iteration in each for loop iteration.
<p>

> **Code**

```py
def insertion_sort(array):
    
    for i in range(1,len(array)):
        temp = array[i]
        j=i-1
        while(temp<array[j] and j>=0):
            array[j+1] = array[j]
            j =j-1
        array[j+1] = temp

    return array    

arr= [6,3,4,1,2]
z=insertion_sort(arr)
print("Insertion_sort: ",z)
```
> **Output**

```
Insertion_sort: [1,2,3,4,6]
```
> **Visual Representation**
```mermaid
flowchart TD
    A([6, 3, 4, 1, 2]) -->|1 iteration| B([3, 6, 4, 1, 2])
    B -->|2 iteration| C([3, 4, 6, 1, 2])
    C -->|3 iteration|D([1, 3, 4, 6, 2])
    D -->|4 iteration| E([1, 2, 3, 4, 6])
```
<hr>


## 2. Bubble Sorting

<p>
In **Bubble Sort** we use two loop i.e.
<pre>
1. for loop: traverse complete array.
|    2. for loop(nested): traverse one element less       
|    |    from the end.
|    |    | if :
</pre>
It sort element in bubble. Bubble contain atmost two element at a time and compair them and sorted. It started with first two element and then second and third and so on.

After completing the first iteration of for loop(not nested one) most of the element take the correct position.

</p>

> **Code**
```py
def bubble_sort(array):
  
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                

    return array    

arr= [6,3,4,1,2]
arr=bubble_sort(arr)
print("Bubble Sort: ", arr)
```

> **Output**
```
Bubble Sort: [1,2,3,4,6]
```
> **Visual Representation**

```mermaid
flowchart TD
    A([6, 3, 4, 1, 2]) -->|1 iteration| B([3, 6, 4, 1, 2])
    B -->|2nd iteration| C([3, 4, 6, 1, 2])
    C -->|3rd iteration| D([3, 4, 1, 6, 2])
    D -->|4th iteration| E([3, 4, 1, 2, 6])
    E -->|5th iteration| F([3, 4, 1, 2, 6])
    F -->|6th iteration| G([3, 1, 4, 2, 6])
    G -->|7th iteration| H([3, 1, 2, 4, 6])
    H -->|8th iteration| I([3, 1, 2, 4, 6])
    I -->|9th iteration| J([1, 3, 2, 4, 6])
    J -->|10th iteration| K([1, 2, 3, 4, 6])
    K -->|11th iteration| L([1, 2, 3, 4, 6])
    L -->|12th iteration| M([1, 2, 3, 4, 6])
    M -->|13th iteration| N([1, 2, 3, 4, 6])
    N -->|14th iteration| O([1, 2, 3, 4, 6])
    O -->|15th iteration| P([1, 2, 3, 4, 6])
    P -->|16th iteration| Q([1, 2, 3, 4, 6])
    Q -->|17th iteration| R([1, 2, 3, 4, 6])
    R -->|18th iteration| S([1, 2, 3, 4, 6]) 
    S -->|19th iteration| T([1, 2, 3, 4, 6])
    T -->|20th iteration| U([1, 2, 3, 4, 6])
```
<br>

## 2.1 Optimise Bubble Sort
<p>
An **flag** element is introduce inside first for loop, whose initial value is "0". If nested loop conditional statement execute the value of **flag** changed then loop work as typical bubble sort.

<pre>
1. for loop: traverse complete array.
|    2. for loop(nested): traverse one element less       
|    |    from the end.
|    |    | if :
|     if : break
</pre>

For a condition the nested for loop conditional statement does not execute than the flag value is unchanged. After completing nested loop the pointer executed the conditional statement of first for loop and break it.  


</p>

> **Code**
```py
def optimize_bubble_sort(array):

    for i in range(len(array)):
        flag =0
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                flag=1
        if flag == 0:
            break
    return array


arr= [6,3,4,1,2]
arr = optimize_bubble_sort(arr)
print("Optimize Bubble Sort: ",arr)
```

> **Output**
```
Bubble Sort: [1,2,3,4,6]
```
> **Visual Representation**

```mermaid
flowchart TD
    A([6, 3, 4, 1, 2]) -->|1 iteration| B([3, 6, 4, 1, 2])
    B -->|2nd iteration| C([3, 4, 6, 1, 2])
    C -->|3rd iteration| D([3, 4, 1, 6, 2])
    D -->|4th iteration| E([3, 4, 1, 2, 6])
    E -->|5th iteration| F([3, 4, 1, 2, 6])
    F -->|6th iteration| G([3, 1, 4, 2, 6])
    G -->|7th iteration| H([3, 1, 2, 4, 6])
    H -->|8th iteration| I([3, 1, 2, 4, 6])
    I -->|9th iteration| J([1, 3, 2, 4, 6])
    J -->|10th iteration| K([1, 2, 3, 4, 6])
    K -->|11th iteration| L([1, 2, 3, 4, 6])
    L -->|12th iteration| M([1, 2, 3, 4, 6])
    M -->|13th iteration| N([1, 2, 3, 4, 6])
    N -->|14th iteration| O([1, 2, 3, 4, 6])
    O -->|15th iteration| P([1, 2, 3, 4, 6])
    P -->|16th iteration| Q([1, 2, 3, 4, 6])
```
<hr>

## 3. Selection Sort
<p>

</p>

> **Code**
```py

```

> **Output**
```

```
> **Visual Representation**

```mermaid

```
<hr>

## 4. Merge Sort
<p>

</p>

> **Code**
```py

```

> **Output**
```

```
> **Visual Representation**

```mermaid

```
<hr>

## 5. Quick Sort

<p>

</p>

> **Code**
```py

```

> **Output**
```

```
> **Visual Representation**

```mermaid

```
<hr>