def main():
    try:
        correct_answer=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
        count_correct,count_student,incorect_answer=test_answer(correct_answer)
        ###########################################################
        print(f'The total number of correctly answered questions are {count_correct}')
        print(f'The total number of incorrectly answered questions are {count_student}')
        print()
        if count_correct>=15:
            print("passed the exam")
        else:
            print("failed the exam")
        print()
        print(f'List showing the question numbers of the incorrectly answered questions:-')
        print(incorect_answer)
    except Exception as l:
        print(l)
def read_student_answer():
    try:
        num=20
        count=0
        stu_answer=[0]*num
        answer=open('student_answer.txt','r')
        answer_f=answer.readlines()
        answer.close()
        ##############################
        for ans in range(num):
            answer_f[ans]=answer_f[ans].lstrip(f'{count+1}.')
            answer_f[ans]=answer_f[ans].rstrip('\n')
            count+=1
        return answer_f,num
    except Exception as k:
        print(k)
def test_answer(correct_answer):
    try:
        count_correct=0
        count_student=0
        incorect_answer=[]
        stud_answer,num=read_student_answer()
        for n in range(num):
            if stud_answer[n]==correct_answer[n]:
                count_correct+=1
            else:
                count_student+=1
                incorect_answer.append(n+1)
        return count_correct,count_student,incorect_answer
    except Exception as j:
        print(j)
main()






