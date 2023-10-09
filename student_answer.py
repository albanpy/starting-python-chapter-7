def main():
    try:
        num=20
        stu_answer=[0]*num
        print('Answer only in capital Letter')
        print()
        for n in range(num):
            stu_answer[n]=input(f"Enter correct answer for question {n+1}.")  
        answer_questions(stu_answer)   
    except Exception as k:
        print(k)
    else:
        print('finshed to answer exam!!')
def answer_questions(student_answer):
    try:
        count=0
        answer=open('student_answer.txt','w')
        for ans in student_answer:
            answer.write(f'{count+1}.{ans}\n')
            count+=1
        answer.close()
    except Exception as j:
        print(j)
main()