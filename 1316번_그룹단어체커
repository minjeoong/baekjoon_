for _ in range(i): 
  word = input()
  error = 0 
  for index in range(len(word)-1): # 0부터 단어길이 - 1 만큼 인덱스를 설정. 
    if word[index] != word[index+1]: #지금 현재 단어가 다음 단어와 다르다면
      new = word[index+1:] #현재단어에서 끊어서 다음 단어를 새로 만듦
      if new.count(word[index]): #현재 알파벳이 새로만든 단어에 있다면 , 즉 연속되지 않고 또 등장했다면
        error += 1 #에러횟수 증가
  if error == 0 :  #에러가 0 이면 그룹단어
    group += 1
print(group)
