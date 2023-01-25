w = input().upper()
uniq_word= list(set(w)) #단어의 중복값을 모두 제거한 값을저장해 놓음. 
al_list = []

for x in uniq_word: # 중복값을 제거한 단어들 중에 , 입력받은 값중에서 같은 값을 카운트 해서 카운트 리스트를 생성.
  cnt = w.count(x)
  al_list.append(cnt)
if al_list.count(max(al_list)) > 1: #만약에 카운트 리스트중에 가장 큰 값의 갯수가 여러개이면 (유일하지 않다면) ? 출력
  print("?")
else: # 아니라면, 카운트 리스트 안에 가장 큰 값의 인덱스를 맥스인덱스로 잡고, 맥스 인덱스에 해당하는 알파벳이 무엇인지 (중복을 제거한 단어리스트)에서 찾기
  max_index = al_list.index(max(al_list))
  print(uniq_word[max_index])
