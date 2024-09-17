def merge_(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i, j = 0, 0
    lst = []
    while (i < m and j < n ):
        if nums1[i] > nums2[j]:
            lst.append(nums2[j])
            j += 1
        elif nums1[i] == nums2[j]:
            lst.append(nums2[j])
            lst.append(nums1[i])
            j += 1
            i += 1
        else:
            lst.append(nums1[i]) 
            i += 1 
    
    if i != m :
        lst += nums1[i:m]
    else:
        lst += nums2[j:n]

    print(i,j,lst)
    
    return lst

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i, j = 0, 0
    while (i < m and j < n ):
        if nums1[i] > nums2[j]:
            nums1.pop()
            nums1.insert(i,nums2[j])
            # lst.append(nums2[j])
            j += 1
            m += 1
        else:
            # lst.append(nums1[i]) 
            i += 1 
    
    # if i != m :
    #     lst += nums1[i:m]
    # else:
    #     lst += nums2[j:n]
    while j <= n-1 :
        nums1.pop()
        nums1.insert(i,nums2[j])
        i += 1
        j += 1

    print(i, j, nums1)

if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 
    merge(nums1, m, nums2, n)

