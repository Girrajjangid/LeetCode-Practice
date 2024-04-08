from collections import deque, Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #count the total sandwiches of each  type  required 
        sandwich_counts = Counter(students)
        #convert to deque, so we pop at 0th index with O(1) time complexity
        sandwich_q = deque(sandwiches)
        students_q = deque(students)
        while sandwich_q and sandwich_counts[sandwich_q[0]] > 0: #students still can eat sandwich
            #sandwich type of student in front of queue
            temp_student = students_q.popleft()
            if temp_student == sandwich_q[0]:
                #if preference mathces
                sandwich_q.popleft()
                #since sandwich is given reduce the count
                sandwich_counts[temp_student] -= 1
            else:
                #take the student to end if no match
                students_q.append(temp_student)
        #return remaining students
        return len(students_q)