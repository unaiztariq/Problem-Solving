def highest_streak(n):
    dictt={}
    count = 1

    for i in range(0,len(n)):

        if n[i] in dictt:
       
                count += 1
                dictt[n[i]].append(i)
        else:
                dictt[n[i]] = [i]
                count = 1

    result = {}
    for key,value in dictt.items():
        no = 1
        nu = 1
    
        for i in range(0,len(value)-1):

            streak = f"{key}.{no}"
            if value[i]+1==value[i+1] :
                nu+=1
                if streak not in result:
                    result[streak]= nu 
                if streak  in result:
                    result[streak]= nu 
                
            else:
                nu = 1
                no += 1
                streak = f"1.{no}"
                if streak not in result:
                    result[streak]= nu

    for i,j in result.items():
        if max(result.values()) == j :
            print(f"the value {i.split('.')[0]} has greatest streak of {j}.")


def run_length_encoding(string):
    dic = {}
    consectives = 0
    result = ""

    for index in range(len(string)):
        keys= f"{consectives}.{string[index]}"
        if f"{consectives}.{string[index]}" in dic :
            values += 1
            dic[keys] = values
        else:
            values = 1
            consectives +=1
            keys= f"{consectives}.{string[index]}"
            dic[keys] = values
    for word,occ in dic.items():
        result += f"({occ},{word.split('.')[1]}) "
    return result

highest_streak("1112233333111111444")
