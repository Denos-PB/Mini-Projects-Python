class Quiz_brain:
    def __init__(self,q_list):
        self.q_num = 0
        self.score = 0
        self.q_list = q_list

    def still_have_q(self):
        return self.q_num < len(self.q_list)


    def next_q(self):
        cur_q = self.q_list[self.q_num]
        self.q_num += 1
        us_ans = input(f"Q.{self.q_num}: {cur_q.text} (True/False): ")
        self.check_answer(us_ans , cur_q.answer)

    def check_answer(self, us_ans , cor_ans):
        if us_ans.lower() == cor_ans.lower():
            print("You got it")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"Corect answear is {cor_ans}")
        print(f"You carrent score is: {self.score}/{self.q_num}")