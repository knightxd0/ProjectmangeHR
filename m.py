from Slinklist import Slinklist
s = Slinklist()

file_rank = open("data/user.txt",encoding="utf8")
rank = file_rank.read()
rank_list = rank.split("\n")
print(rank_list)
for data_r in rank_list:
    s.insertAtEnd(data_r)

s.search("SUMITA SRIPROM")