#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#The class class Point get a tuple named "Point".
#The class class Rectangle let the two points in the input parameter be the diagonal of the rectangle to get the query rectangle.
#The class class Node get a tuple named " Node ".


# In[ ]:


def __init_(self):
    self._root = None
    self._n = 0
def insert_helper (node, point, depth) :
    # If the current node is None, return a new node with the point as the location.
    if node is None:
        return Node(point, Wone, Wone)
    # Determine the axis to split on based on the current depth
    axis = depth % 2
    # If the point is less than the location of the current node along the split axis,and insert the point into the left subtree.
    if point[axis] < node.location[axis]:
        left = insert_helper(node.left, point, depth+1)
        return Node(node.location, left, noderight)
    # Or , insert the point into the right subtree
    else:
        right = insert_helper(node.right, point, depth+1)
        return Node(node.location, node.left, right)
    # Cali the recursive helper function to insert the point
    self._root = insert_helper(self._root, p, 0)
    self._n += 1
#The insert function traverses the tree and finds the appropriate location of the point



#The insert helper function accepts three parameters:



#Node: The current node being checked.



#Point: the point to insert.



#Depth: the current depth of the tree.



#Compare the value of the node of inset.helper function with the position value of the current node. 
#If the point is greater than or equal to the position along the division axis, the branch recursively calls itself on the right subtree


# In[ ]:


def range_helper(node) :
    # If the current node is None, return an empty fist.
    if node is Wone:
        return []
    # Check if the current node's Iocation is within the rectangle.
    if rectangle.is_contains(node.location) :
        points = [node.location]
    else:
        points = []
    # If the rectangle extends to the left of the current node's location, search the left subtree
    if rectangle.lower.x <= node.location.x:
        points += range helper(node.left)
    # If the rectangle eytends to the right of the current node's ocation search the right subtree
    if rectangle.upperx >= node.location.x:
        points += range helper(node.right)
    return points
    # Call the recursive helper function to search for points within the rectangle
    return range_helper(self._root)
#The range function is used to find all points within a given rectangle.
#The range helper function has one parameter:
#Node: The current node being checked.
#The range helper function first checks whether the position of the current node is within the rectangle, at each level of the tree. 
#If so, it adds the position to the color list.


# In[1]:


#the time complexity of range quer:     O(根号n)
#the proof process is showed in extra picture


# In[ ]:


#Suppose now we want to find out one of these points,（3,4.5) The nearest point (this distance can be Euclidean distance.
#It can also be Manhattan distance. Here is the European distance)
#Let's follow the comparison method of KD tree to find one
#The distance between the nearest approximate points (4,7) is r
#Then draw a circle according to the radius of r. Find the following moment
#If the shapes intersect, it is possible that the answer is below
#Next, we find that (2,3) is Nearest point.
#the picture will be showen in the pdf file


# In[ ]:


def divDataToLeftOrRight(self, find_data):
        '''
        Distribute the incoming data to the left node (0) or the right node (1)
        '''
        data_value = find_data[self.split]
        if data_value < self.range:
            return 0
        else:
            return 1
def getSearchPath(self, ls_path, find_data):
        '''
       Binary Find to Leaf Node
        '''
        now_node = ls_path[-1]
        if now_node == None:
            return ls_path
        now_split = now_node.divDataToLeftOrRight(find_data)
        if now_split == 0:
            next_node = now_node.left
        else:
            next_node = now_node.right
        while(next_node!=None):
            ls_path.append(next_node)
            next_split = next_node.divDataToLeftOrRight(find_data)
            if next_split == 0:
                next_node = next_node.left
            else:
                next_node = next_node.right
        return ls_path
            
def getNestNode(self, find_data, min_dist, min_data):
        '''
        The nearest neighbor distance of the backtracking search target point
        '''
        ls_path = []
        ls_path.append(self)
        self.getSearchPath(ls_path, find_data)
        now_node = ls_path.pop()
        now_node.isinvted = True
        min_data = now_node.nodedata
        min_dist = np.linalg.norm(find_data-min_data)
        while(len(ls_path)!=0):
            back_node = ls_path.pop()   ### 向上回溯一个节点
            if back_node.isinvted == True:
                continue
            else:
                back_node.isinvted = True
            back_dist = np.linalg.norm(find_data-back_node.nodedata)
            if back_dist < min_dist:
                min_data = back_node.nodedata
                min_dist = back_dist
            if np.abs(find_data[back_node.split]-back_node.range) < min_dist:
                ls_path.append(back_node)
                if back_node.left.isinvted == True:
                    if back_node.right == None:
                        continue
                    ls_path.append(back_node.right)
                else:
                    if back_node.left == None:
                        continue
                    ls_path.append(back_node.left)
                ls_path = back_node.getSearchPath(ls_path, find_data)
                now_node = ls_path.pop()
                now_node.isinvted = True
                now_dist = np.linalg.norm(find_data-now_node.nodedata)
                if now_dist < min_dist:
                    min_data = now_node.nodedata
                    min_dist = now_dist
        print("min distance:{}  min data:{}".format(min_dist, min_data))
        return min_dist

    def getNestDistByEx(self, test_array, find_data, min_dist, min_data):
        '''
        The Nearest Neighbor Distance of Target Point Obtained by Exhaustion Method
        '''
        data_count = test_array.shape[0]
        min_data = test_array[0]
        min_dist = np.linalg.norm(find_data-min_data)
        for i in range(data_count):
            now_data = test_array[i]
            now_dist = np.linalg.norm(find_data-now_data)
            if now_dist < min_dist:
                min_dist = now_dist
                min_data = now_data
        print("min distance:{}  min data:{}".format(min_dist, min_data))
        return min_dist

